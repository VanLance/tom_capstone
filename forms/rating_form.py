from flask import render_template, SQLAlchemy, Flask
from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField
from wtforms.validators import InputRequired, Rating, Recipe, current_user, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class RatingForm(FlaskForm):
    rating = SelectField('Rating', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
    validators = [InputRequired()]
    review_text = TextAreaField('Review')

@app.route('/recipe/<int:recipe_id>', methods=['GET', 'POST'])
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    rating_form = RatingForm()
    
    if rating_form.validate_on_submit():
        rating = Rating(recipe_id=recipe.id, user_id=current_user.id, rating=rating_form.rating.data, review_text=rating_form.review_text.data)
        db.session.add(rating)
        db.session.commit()
        flash('Thank you for your rating and review!')

    return render_template('recipe_detail.html', recipe=recipe, rating_form=rating_form)
