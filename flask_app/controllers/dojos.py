from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dojos')
def dojos_home():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)

@app.route('/create-dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/one-dojo/<int:id>')
def display_dojo(id):
    data = {
        "id":id
    }
    return render_template('view_dojo.html', dojo = Dojo.get_one_dojo(data))