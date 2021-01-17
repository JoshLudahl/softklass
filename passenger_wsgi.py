import os
from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/privacy-policy')
def hello_world():
    return render_template('privacy-policy.html')

application = app
