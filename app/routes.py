from app import app
from flask import Flask, render_template, request, redirect, session
from app.models import User, Recipe
from app import db
import requests

@app.route('/recipes')
def recipes():
    if 'username' not in session:
        return redirect('/login')
    
    api_key = '962c05fa68eb23f43004c092830548c4189e5bb2'
    url = f'https://suggestic.com/api.html?apiKey={api_key}'

    try:
        response = requests.get(url)
        data = response.json()
        recipes = data['recipes']
    except requests.exceptions.RequestException as error:
        return render_template('error.html', error=error)
    
    return render_template('recipes.html', recipes=recipes)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect('/login')
    
    username = session['username']
    user = User.query.filter_by(username=username).first()

    if request.method == 'POST':
        user.email = request.form['email']
        user.password = request.form['password']
        db.session.commit()
        return redirect('/profile')
    
    return render_template('profile.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['username'] = username
            return redirect('/')
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' not in session:
        return redirect('/')

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('register.html', error='Username already exists')

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        session['username'] = username
        return redirect('/')
    
    return render_template('register.html')    
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

    


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect('/')
        else:
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')


@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        return f'Welcome, {username}! <a href="/logout">Logout</a>'
    else:
        return 'Hello, please <a href="/login">login</a> or <a href="/register">register</a>'



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

    
def get_recipe(recipe_id):
    return f"Recipe{recipe_id}"
