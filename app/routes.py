from flask import render_template, flash, redirect, request, url_for
from app import app
from app.forms import CodeForm
import sqlite3 as sql
import os


def save(path,queries):
    f = open(path, "w")
    for line in queries.splitlines():
        f.write(line+'\n')
    f.close()

def findCreatedTables(queries, conn):
    tablelst = []
    querylst = queries.split()
    nameIndices = [i+1 for i in range(len(querylst)) if i != 0 and querylst[i-1].lower()=="create" and querylst[i].lower()=="table"]
    for index in nameIndices:
        table = [querylst[index]]
        try:
            result = conn.cursor().execute(f"select * from {querylst[index]}")
            table.append([row for row in result])
            tablelst.append(table)
        except sql.Error as e:
            flash(f"SQL Error: {e}")
    return tablelst

def get_sql_files():
    dirs = os.listdir(os.getcwd())
    return [d for d in dirs if '.sql' in d]

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CodeForm()
    files=get_sql_files()
    data = []
    createdTables = []
    if form.validate_on_submit():
        if form.run.data:
            open('database.db', 'w').close()
            with sql.connect('database.db') as conn:
                queries = form.code.data
                for query in queries.split(";"):
                    try:
                        results = conn.cursor().execute(query)
                        resultTable = [row for row in results]
                        if resultTable:
                            data.append(resultTable)
                    except sql.Error as e:
                        flash(f"SQL Error: {e}")
                createdTables = findCreatedTables(queries, conn)
            save("example.sql",queries)
        if form.save.data:
            queries = form.code.data
            save("example.sql",queries)

    return render_template('index.html', title='Home', files = files, createdTables = createdTables, data=data, form=form)
