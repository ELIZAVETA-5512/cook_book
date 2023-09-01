import os
from pathlib import Path
from pprint import pprint


code_type = "utf-8"
url = "recipes.txt"
cook_book = {}


def create_cookbook(url, code_type):
    cook_book = {}
    ingredients_dict = {}
    dish_ingredients_list = []
    next_dish = True

    with open(url, "r", encoding=code_type) as recipes_list:

        for line in recipes_list:

            if next_dish == True:
                cook_book[line.rstrip()] = []
                dish_name = line.rstrip()
                dish_ingredients_list.clear()
                next_dish = False

            elif "|" in line:
                ingredients_row = line.split('|')
                ingredients_dict['ingredient_name'] = ingredients_row[0].rstrip()
                ingredients_dict['quantity'] = int(ingredients_row[1].rstrip())
                ingredients_dict['measure'] = ingredients_row[2].rstrip()
                dish_ingredients_list.append(ingredients_dict.copy())
                ingredients_dict.clear()

            elif line == '\n':
                next_dish = True

            cook_book[dish_name] = (dish_ingredients_list.copy())

        return cook_book
