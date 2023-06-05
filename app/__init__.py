from flask import Flask, render_template
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import db, request, redirect

app = Flask(__name__)
db = SQLAlchemy(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(50), nullable=False)
    instructions =db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Recipe'{self.title}'"

@app.route('/')
def home():
    recipes = Recipe.query.all()
    return render_template('base.html', recipes=recipes)

@app.route('/recipe/recipe_id=integer')
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe_detail.html', recipe=recipe)

@app.route('/recipe/add', method=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        author = request.form['author']
        add_recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions, author=author)
        db.session.add(add_recipe)
        db.session.commit()
        return redirect('/')
    return render_template('add_recipe.html')

if __name__ == '__main__':
    app.run(debug=True)
