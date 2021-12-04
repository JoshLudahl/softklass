from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inxex():
    return render_template('index.html')

@app.route('/privacy-policy')
def privacy():
    return render_template('privacy-policy.html')

application = app
