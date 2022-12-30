from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

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

@app.route('/delete/<int:id>')
def delete_ninja(id):
    data = {
        "id":id
    }
    Ninja.delete(data)
    return redirect('/dojos')

@app.route('/go-edit/<int:id>')
def go_edit_ninja(id):
    data = {
        "id":id
    }
    return render_template('edit_ninja.html', ninja = Ninja.get_one_ninja(data))

@app.route('/edit-one-ninja', methods = ["POST"])
def update_ninja():
    Ninja.update(request.form)
    return redirect('/dojos')

