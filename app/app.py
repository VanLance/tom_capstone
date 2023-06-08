from flask import Flask, render_template, request, redirect, url_for
from app.config import Config
from app import app

app = Flask(__name__)
app.config.from_object(Config)

recipes = [
    {
        'title': 'Pasta Carbonara',
        'ingredients': ['spaghetti', 'bacon', 'eggs', 'parmesan cheese'],
        'instructions': '1. Cook spaghetti according to the cooking book instructions. ...',
        'author': 'Mario Fibonacci'
    },
    {
        'title': 'Chocolate Chip Cookies',
        'ingredients': ['butter', 'sugar', 'flour', 'chocolate chips'],
        'instructions': '1. Preheat oven to 375ºF. ...',
        'author': 'Luigi Fibonacci'
    }
]

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients'].split(',')
        instructions = request.form['instructions']
        author = request.form['author']

        new_recipe = {
            'title': title,
            'ingredients': ingredients,
            'instructions': instructions,
            'author': author
        }

        recipes.append(new_recipe)

        return redirect(url_for('index'))
    
    return render_template('add_recipe.html')

if __name__ == '__main__':
    app.run()

# Pasta Carbonara
# STEP 1: Cook pasta according to package directions. Drain well and set aside.
# STEP 2: Meanwhile, place bacon in large skillet. Add butter and Garlic Paste. 
# Cook on medium heat bacon is cooked through and lightly browned.
# STEP 3: Whisk egg yolks, heavy cream, Parmesan, Basil Paste and Italian Herb Paste in medium bowl until well blended.
# STEP 4: Add hot cooked pasta to skillet with bacon, tossing to mix well. 
# Gradually add egg mixture, tossing to mix well and heat through. 
# Serve immediately.

# Chocolate Chip Cookies
# 1. Stir flour with baking soda and salt; set aside.
# 2. In large mixing bowl, beat butter with sugar, and brown sugar at medium speed until creamy and lightened in color.
# 3. Add eggs and vanilla, one at a time. Mix on low speed until incorporated.
# 4. Gradually blend dry mixture into creamed mixture. Stir in nuts and chocolate chips.
# 5. Drop by tablespoon onto ungreased cookie sheets.
# 6. Bake for 9 to 11 minutes or until chocolate chip cookies are golden brown.

# Internet Source: www.gourmetgarden.com
# Internet Source: www.ghirardelli.com
