from flask import Blueprint
from flask import Flask

app = Flask(__name__)
recipe_blueprint = Blueprint('recipe', __name__)
app.register_blueprint(recipe_blueprint, url_prefix='/recipe')

@recipe_blueprint.route('/recipe/<recipe_id>')
def index():
    return 'Hello, welcome to the recipe sharing platform'

def get_recipe(recipe_id):
    return f"Recipe{recipe_id}"
