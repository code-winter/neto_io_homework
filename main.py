def get_recipes_dict(filename, mode, encode):
    recipe_dict = dict()
    dish = str()
    ingredient = str()
    quantity = str()
    amount = str()
    measure = str()
    buffer_list = list()
    with open(filename, mode, encoding=encode) as file:
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
    temp_list = list()
    for dish_name in dishes:
        for dish, ingredient in cook_dict.items():
            if dish == dish_name:
                pass

    return 0


path = 'recipes.txt'
encoding_type = 'utf-8'
mode = 'r'
cook_book = get_recipes_dict(path, mode, encoding_type)
print(cook_book)




