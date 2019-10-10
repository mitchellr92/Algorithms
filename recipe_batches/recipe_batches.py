#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  all_batches = []

  # Compare length of both dictionaries
  if len(recipe) != len(ingredients):
    # If lengths are not even, return 0
    return 0

  # Compare values of matching ingredient names in both dictionaries
  for rec_key, rec_value in recipe.items():
    for ingr_key, ingr_value in ingredients.items():
      if rec_key == ingr_key:
        # Divide each rec value by each matching ingr value
        current_batches = ingr_value / rec_value
        all_batches.append(current_batches)

  # Take lowest quotient and set batches to that value
  batches = min(float(num) for num in all_batches)
  batches = math.floor(batches)
  print(batches)
  
  # If lowest quotient is less than 1, return 0
  if batches < 1:
    return 0

  return batches


rec = { 'milk': 2, 'butter': 20, 'sugar': 40 }
ingr = { 'milk': 5, 'sugar': 120, 'butter': 500 }

recipe_batches(rec, ingr)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))