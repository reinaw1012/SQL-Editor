from flask import render_template, flash, redirect, request, url_for
from app import app
from app.forms import CodeForm
import sqlite3 as sql

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CodeForm()
    data = ""
    if form.validate_on_submit():
        open('database.db', 'w').close()
        with sql.connect('database.db') as conn:
            queries = form.code.data
            data = []
            for query in queries.split(";"):
                results = conn.cursor().execute(query)
                for row in results:
                    line=" | ".join(row)
                    data.append(line)
        f = open("example.sql", "w")
        f.write(queries)
        f.close()
    return render_template('index.html', title='Home', data=data, form=form)
