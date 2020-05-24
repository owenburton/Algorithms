#!/usr/bin/python

import math

def recipe_batches(r, i):
  # set a lowest value equal to the first item number in ingredients divided by first in recipe (no remainder)
  # iterate through the number of items in one of the dicts
  # if at any point ingredient count divided by (no remainder) recipy ingredient count is 
  # lower than the current lowest val, change lowest val to that number
  # return lowest

  # also account for if stock doesn't include one of the recipe ingredients
  if len(r)>len(i):
    return 0
  low = list(i.values())[0] // list(r.values())[0]
  for x in range(len(r)):
    current = list(i.values())[x] // list(r.values())[x]
    if current < low:
      low = current
  return low

  

   

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))