from app import app
from flask import render_template

@app.route('/')

@app.route('/index')
def index():
    return "index"
    return render_template("index.html")

@app.route('/about')
def about():
    return "about"
    return render_template("about.html")

@app.route('/contacts')
def contacts():
    return "contacts"
    return render_template("contacts.html")