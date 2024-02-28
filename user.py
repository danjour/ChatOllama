from flask import Flask, render_template, session, redirect, url_for, request
from db import * 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        success, name = read_user(login, password)
        if success:
            name_parts = name.split()
            initials = [part[:1] for part in name_parts if part]
            session['login'] = login
            session['name'] = name
            session['initials']=''.join(initials)
            session['logged_in'] = True

            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid login or password.") 
    else:
        return render_template('login.html')
    
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        name = request.form['name']
        login = request.form['login']
        password = request.form['password']
        save_user(login, password,name)
        
        return redirect(url_for('login'))
    else:
        return render_template('register.html')