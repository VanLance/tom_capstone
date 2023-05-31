from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy impport SQLAlchemy
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password =db.Column(db.String(50), nullable=False)

@app.route('/recipes')
def recipes():
    if 'username' not in session:
        return redirect('/login')
    
    api_key - '962c05fa68eb23f43004c092830548c4189e5bb2'
    url = f'https://suggestic.com/api.html?apiKey={api_key}'

    try:
        response = requests.get(url)
        data = response.json()
        recipes = data['recipes']
    except requests.exceptions.RequestException as error:
        return render_template('error.html', error=error)
    
    return render_template('recipes.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True, host='suggestic.com')
