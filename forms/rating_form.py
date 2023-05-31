from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField
from wtforms.validators import InputRequired

class RatingForm(FlaskForm):
    rating = SelectField('Rating', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
    validators = [InputRequired()]
    review_text = TextAreaField('Review')
