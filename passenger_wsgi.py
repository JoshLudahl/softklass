import os
from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():

    resp = render_template('index.html')
    return resp

application = app


