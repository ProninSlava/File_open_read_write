from pprint import pprint
import os
def make_cook_book(name_file):
    cook_book = {}
    with open(name_file, encoding='UTF-8') as file:
        for i in file:
            name_dish = i.strip()
            quantity = int(file.readline())
            cook_book[name_dish] = []
            for i in range(quantity):
                data = file.readline().split(' | ')
                ingredients = {'ingredient_name': data[0], 'quantity': int(data[1]), 'measure': data[2].strip()}
                cook_book[name_dish].append(ingredients)
            file.readline()

    return cook_book

pprint(make_cook_book('recipes.txt'))

