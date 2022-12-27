from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dojos')
def dojos_home():
    return render_template('dojos.html')

@app.route('/ninjas')
def create_ninja():
    return render_template('create_ninja.html')



if __name__ == "__main__":
    app.run(debug=True)