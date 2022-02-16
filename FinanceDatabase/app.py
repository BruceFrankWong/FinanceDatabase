# -*- coding: UTF-8 -*-

__author__ = 'Bruce Frank Wong'


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/performance')
def performance():
    return render_template('index.html')


@app.route('/research')
def research():
    return render_template('index.html')


@app.route('/report')
def report():
    return render_template('index.html')