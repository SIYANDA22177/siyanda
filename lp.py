from flask import FlASK, request, render_templet
import sqlite3
import os

current = os.path.dirname(os.path.abspath(__file__))

app = FlASK(__name__)

@pp.route('/')
def home():
    return render_templet('lp.py')


@pp.rout('/', methods =["POST","GET"])
def lo():
    name = request.form("fname")
    email = request.form("femail")
    call = request.form("fcall")
    
#creat connection
connection = sqlite3.connect(current + "\siyanda.db")
#ACTIVATE CURS
cur = connection.cursor()
cur.execute("insert int data(call, email,name)"values(?,?,?)) ,(call,email,name)
connection.commit()
                                                      

    return render_templet("lohtml")
if __name__ == " _main ":
    app.run(debug=True)