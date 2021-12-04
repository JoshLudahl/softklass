import json, os, requests
from flask import Flask, make_response, redirect, render_template, request, session, url_for

zipCodes = ZipCodeDatabase()

app = Flask(__name__)

@app.route('/')
def inxex():
    return render_template('index.html')

@app.route('/privacy-policy')
def privacy():
    return render_template('privacy-policy.html')

application = app
