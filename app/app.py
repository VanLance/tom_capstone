from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
        'instructions': '1. Preheat oven to 375. ...',
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
# STEP 1
# Boil the pasta. Meanwhile, fry pancetta in oil in a frying pan for a few mins until golden and crisp. Add garlic, fry for 1 min, then turn off the heat. Briefly whisk egg and yolks with most of the Parmesan and some seasoning.

# STEP 2
# Drain pasta, reserving a little of the cooking water. Add eggs and a tap of cooking water, then mix until pasta is coated and creamy. The heat from the pasta will gently cook the sauce. Stir in the pancetta and garlic then serve, topped with the remaining Parmesan.

# Chocolate Chip Cookies
# 1. Beat the butter and sugars, then beat in the eggs and vanilla.
# 2. Dissolve the baking soda in hot water and add to the mixture.
# 3. Stir in the flour, chocolate chips, and walnuts.
# 4. Drop dough onto a prepared baking sheet.
# 5. Bake until the edges are golden brown.
