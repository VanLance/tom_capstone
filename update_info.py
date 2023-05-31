from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password =db.Column(db.String(50), nullable=False)

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

if __name__ == '__main__':
    app.run(debug=True)

# Provide the user to update their information and a way for users to sign up for the application.
