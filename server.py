from flask import Flask, render_template, request, redirect
from dojo import Dojo
from ninja import Ninja
app = Flask(__name__)

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



if __name__ == "__main__":
    app.run(debug=True)