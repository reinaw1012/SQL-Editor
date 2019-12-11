from flask import render_template, flash, redirect, request, url_for
from app import app
from app.forms import CodeForm
import sqlite3 as sql

# def displayTable(query, conn):
#     """ Returns a list of lists, where every nested list represents a row in the displayed table
#     Arguments:
#         query {str} -- a "create table" string query
#     Returns:
#         list -- represents the table created from the query
#     """
#     querylst = query.split()
#     title = querylst[2]
#     if querylst[3][0] == '(': #standard create table statement
#         if querylst[3] == '(':
#             querylst.pop(3)
#         else: 
#             querylst[3] = querylst[3][1:]
#         if querylst[-1] == ';':
#             querylst.pop(-1)
#             if querylst[-1] == ')':
#                 querylst.pop(-1)
#             else: 
#                 querylst[-1] = querylst[-1][:-1]
#         elif querylst[-1] == ');':
#             querylst.pop(-1)
#         else:
#             querylst[-1] = querylst[-1][:-2]
#         tablelst = querylst[3::2]
#     elif querylst[3].lower() == 'as': # AS create table statement
#         index = query.lower().find(querylst[4].lower())
#         result = conn.cursor().execute(query[index:])
#         tablelst = [row for row in result]
#     else:
#         pass # Are there any other ways to create tables
#     return title, tablelst

def save(path,queries):
    f = open(path, "w")
    f.write(queries)
    f.close()

def findCreatedTables(queries, conn):
    tablelst = []
    querylst = queries.lower().split()
    nameIndices = [i+1 for i in range(len(querylst)) if i != 0 and querylst[i-1]=="create" and querylst[i]=="table"]
    for index in nameIndices:
        table = [querylst[index]]
        try:
            result = conn.cursor().execute(f"select * from {querylst[index]}")
            table.append([row for row in result])
            tablelst.append(table)
        except sqlite3.Error as e:
            print("SQL Error: ", e)
    return tablelst


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CodeForm()
    data = []
    createdTables = []
    if form.validate_on_submit():
        if form.run.data:
            open('database.db', 'w').close()
            with sql.connect('database.db') as conn:
                queries = form.code.data
                for query in queries.split(";"):
                    # if "create table" in query.lower():
                    #     title, table = displayTable(query, conn)
                    #     createdTables.append([title,table])
                    try:
                        results = conn.cursor().execute(query)
                        resultTable = [row for row in results]
                        if resultTable:
                            data.append(resultTable)
                    except sqlite3.Error as e:
                        print("SQL Error: ", e)
                createdTables = findCreatedTables(queries, conn)
                # print(findCreatedTables(queries, conn))
                # print("===========")
                # print(createdTables)
            save("example.sql",queries)
        if form.save.data:
            queries = form.code.data
            save("example.sql",queries)

    return render_template('index.html', title='Home', createdTables = createdTables, data=data, form=form)
