from app import app
from flask import Flask, render_template, redirect, url_for, request


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

#@app.route('/forms')
#def forms():
 #   return render_template("forms.html")

# Route for handling the login page logic
@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] !='admin':
            error = 'Dados inválidos. Por favor, tente novamente!'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error = error)