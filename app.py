from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html')

@app.route('/restaurants')
def restaurants():
    return render_template('restaurants.html')

@app.route('/chefs')
def chefs():
    return render_template('chefs.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
