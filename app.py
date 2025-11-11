import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Megan Y. in 3308!'

@app.route("/db_test")
def testing():
    conn = psycopg2.connect("postgresql://lab10_postgres_u2h2_user:VovgFrTTMOVbWjwgv3yxZXM608XkNnmK@dpg-d49mrue3jp1c73e4sa70-a/lab10_postgres_u2h2")
    conn.close()
    return "Database connection successful"

@app.route("/db_create")
def create():
    conn = psycopg2.connect("postgresql://lab10_postgres_u2h2_user:VovgFrTTMOVbWjwgv3yxZXM608XkNnmK@dpg-d49mrue3jp1c73e4sa70-a/lab10_postgres_u2h2")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
    );
    ''')
    
    conn.commit()
    conn.close()
    return("Basketball Table Successfully Created")
