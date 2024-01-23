from functools import reduce

# Immutable data structure representing ingredients
class PastaRecipe:
    def __init__(self, ingredients):
        self.ingredients = ingredients

# Side-effect-free function to create a PastaRecipe
def create_recipe(ingredients):
    return PastaRecipe(ingredients)

# Higher-order function to add an ingredient to the recipe
def add_ingredient(recipe, ingredient):
    new_ingredients = recipe.ingredients + [ingredient]
    return create_recipe(new_ingredients)

# Function to print the ingredients of a recipe
def print_ingredients(recipe):
    print("Ingredients:", recipe.ingredients)

# Higher-order function to filter ingredients based on a condition
def filter_ingredients(recipe, condition):
    filtered_ingredients = list(filter(condition, recipe.ingredients))
    return create_recipe(filtered_ingredients)

# Function as a parameter - Predicate function to check if an ingredient is a vegetable
is_vegetable = lambda ingredient: ingredient.lower() in ["tomato", "onion", "spinach", "bell pepper"]

# Function as a parameter - Transformation function to capitalize all ingredients
capitalize_ingredient = lambda ingredient: ingredient.capitalize()

# Higher-order function to apply a transformation to all ingredients
def transform_ingredients(recipe, transformation):
    transformed_ingredients = list(map(transformation, recipe.ingredients))
    return create_recipe(transformed_ingredients)

# Use of closures - Create a function that returns a function to add a specific ingredient
def add_specific_ingredient(ingredient):
    def add_ingredient_to_recipe(recipe):
        return add_ingredient(recipe, ingredient)
    return add_ingredient_to_recipe

# Example usage:
initial_ingredients = ["pasta", "tomato sauce", "cheese"]
recipe = create_recipe(initial_ingredients)

# Adding ingredients using higher-order function
recipe_with_meat = add_specific_ingredient("chicken")(recipe)
recipe_with_veggies = add_specific_ingredient("spinach")(recipe_with_meat)

# Filtering ingredients using higher-order function
vegetarian_recipe = filter_ingredients(recipe_with_veggies, is_vegetable)

# Transforming ingredients using higher-order function
capitalized_recipe = transform_ingredients(vegetarian_recipe, capitalize_ingredient)

# Printing final ingredients
print_ingredients(capitalized_recipe)
