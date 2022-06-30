from pprint import pprint
import os


def open_file():
    file_dir = os.path.join(os.getcwd(), 'recipes.txt')
    key_list = ['ingredient_name', 'quantity', 'measure']
    cook_book = {}

    with open(file_dir) as file:
        for line in file:
            ingr_list = []
            dish_name = line.strip()
            quantity = int(file.readline())
            for ingredients in range(quantity):
                ingr_str = str(file.readline().strip()).split('|')
                ingr_write = {key_list[item]: ingr_str[item] for item in range(len(key_list))}
                ingr_list.append(ingr_write)
            file.readline()
            cook_book[dish_name] = ingr_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = open_file()
    ingr_dict = {}
    for dish_name in dishes:
        for ingr in cook_book[dish_name]:
            ingredient = ingr['ingredient_name']
            quantity = int(ingr['quantity']) * person_count
            measure = ingr['measure']
            if ingredient not in ingr_dict.keys():
                ingr_dict[ingredient] = {'quantity': quantity, 'measure': measure}
            else:
                ingr_dict[ingredient]['quantity'] += quantity

    return ingr_dict


pprint(open_file())
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос', 'Фахитос'], 3))