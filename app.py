from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
import uuid
import sqlite3
from datetime import datetime, timezone
from random import randint
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = '14806762'


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aihiring')
def aihiring():
    return render_template("aihiring.html")

@app.route('/dilemmas')
def dilemas():
    return render_template("dilemmas.html")

@app.route('/solutions')
def solutions():
    return render_template("solutions.html")


if __name__ == '__main__':
    app.run(debug=True, port=5006)