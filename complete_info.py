from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy impport SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password =db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

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

if __name__ == '__main__':
    app.run(debug=True)
    
# These methods been added to make a clean user interface(UI) The homepage renders the index.html template to display an overview of the recipe sharing platform and any other information that's relevant.
# /recipes renders the recipes.html template to display a list of recipes from the third-party or your own database.
# /profiles allows users to view and update their profile information.
# /login allows the user to login to view their recipe. /register allows the user to sign up for the recipe view. /logout allows the user to sign out of the application.
