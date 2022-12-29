from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all()
    return render_template('create_ninja.html', dojos = dojos)

@app.route('/create-ninja', methods = ["POST"])
def save_ninja():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    Ninja.save(data)
    return redirect('/dojos')