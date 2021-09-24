def get_recipes_dict(filename, mode_type, encode):
    with open(filename, mode_type, encoding=encode) as file:
        recipe_dict = dict()
        for line in file:
            dish = line.strip()
            amount = int(file.readline())
            buffer_list = list()
            for item in range(amount):
                ingredient, quantity, measure = file.readline().split('|')
                buffer_list.append(
                    {'ingredient_name': ingredient.strip(), 'quantity': int(quantity), 'measure': measure.strip()}
                )
            recipe_dict[dish] = buffer_list
            file.readline()
    return recipe_dict


def get_shop_list_by_dishes(cook_dict, dishes, person_count):
    temp_dict = dict()
    for dish_name in dishes:
        for dish_type, ingredient_list in cook_dict.items():
            if dish_type == dish_name:
                for ingr_dict in ingredient_list:
                    ingr_name = ingr_dict['ingredient_name']
                    if temp_dict.setdefault(ingr_name) is None:
                        temp_dict[ingr_name] = {
                            'quantity': ingr_dict['quantity'] * person_count, 'measure': ingr_dict['measure']
                        }
                    else:
                        temp_dict[ingr_name]['quantity'] += ingr_dict['quantity'] * person_count
    return temp_dict


path = 'recipes.txt'
encoding_type = 'utf-8'
mode = 'r'
cook_book = get_recipes_dict(path, mode, encoding_type)
print(cook_book)
test = get_shop_list_by_dishes(cook_book, ['Омлет', 'Запеченный картофель'], 3)
print(test)



