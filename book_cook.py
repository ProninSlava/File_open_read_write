from pprint import pprint
import os

def make_cook_book(name_file):
    with open(name_file, encoding='UTF-8') as f:
        cook_book = {}
        for line in f:
            if len(line) > 2 and '|' not in line:
                name_dish = line.strip()
                if name_dish not in cook_book:
                    cook_book[name_dish] = []
            elif '|' in line:
                data = line.strip().split('|')
                ingredients = {'ingredient_name': data[0], 'quantity': data[1], 'measure': data[2]}
                cook_book[name_dish].append(ingredients)

        return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = make_cook_book('recipes.txt')
    ingredients_dict = {}
    for name_dishes in dishes:
        if name_dishes in cook_book:
             for d in cook_book[name_dishes]:
                if d['ingredient_name'] not in ingredients_dict:
                    ingredients_dict[d['ingredient_name']] = {'measure':d['measure'], 'quantity': int(d['quantity']) * person_count}
                else:
                    ingredients_dict[d['ingredient_name']]['quantity'] += int(d['quantity']) * person_count
    pprint(ingredients_dict)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)