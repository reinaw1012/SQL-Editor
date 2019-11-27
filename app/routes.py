from flask import render_template, flash, redirect, request, url_for
from app import app
from app.forms import CodeForm
import sqlite3 as sql

def displayTable(query, conn):
    """ Returns a list of lists, where every nested list represents a row in the displayed table
    Arguments:
        query {str} -- a "create table" string query
    Returns:
        list -- represents the table created from the query
    """
    querylst = query.split()
    title = querylst[2]
    if querylst[3][0] == '(': #standard create table statement
        if querylst[3] == '(':
            querylst.pop(3)
        else: 
            querylst[3] = querylst[3][1:]
        if querylst[-1] == ';':
            querylst.pop(-1)
            if querylst[-1] == ')':
                querylst.pop(-1)
            else: 
                querylst[-1] = querylst[-1][:-1]
        elif querylst[-1] == ');':
            querylst.pop(-1)
        else:
            querylst[-1] = querylst[-1][:-2]
        tablelst = querylst[3::2]
    elif querylst[3].lower() == 'as': # AS create table statement
        index = query.lower().find(querylst[4].lower())
        result = conn.cursor().execute(query[index:])
        tablelst = [row for row in result]
    else:
        pass # Are there any other ways to create tables
    return title, tablelst


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CodeForm()
    data = []
    createdTables = []
    if form.validate_on_submit():
        open('database.db', 'w').close()
        with sql.connect('database.db') as conn:
            queries = form.code.data
            for query in queries.split(";"):
                if "create table" in query.lower():
                    title, table = displayTable(query, conn)
                    createdTables.append([title,table])
                results = conn.cursor().execute(query)
                data.append([row for row in results])
        f = open("example.sql", "w")
        f.write(queries)
        f.close()
    return render_template('index.html', title='Home', createdTables = createdTables, data=data, form=form)
