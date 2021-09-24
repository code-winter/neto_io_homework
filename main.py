def get_recipes_dict(filename, mode_type, encode):
    """
    Gets formatted nested dictionary from file

    :param filename: name of file
    :param mode_type: parameter for mode
    :param encode: utf-8 encoding
    :return: returns dictionary with recipes
    """
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
    """
    Gets a dictionary from recipes dictionary and changes number of ingredients

    :param cook_dict: recipes dict
    :param dishes: list of dish names
    :param person_count: amount of servings
    :return: returns formatted dictionary with modified amounts of quantity
    """
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


def count_lines(filename):
    """
    Counts lines in a file

    :param filename: file name in str format
    :return: returns tuple with (text_name:number_of_lines)
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines_count = int()
        for line in file:
            lines_count += 1
        info_tuple = (filename, lines_count)
    return info_tuple


def get_text(filename):
    """
    Reads text from file and returns it

    :param filename: file name in str format
    :return: returns list with text
    """
    with open(filename, 'r', encoding='utf-8') as file:
        file_text = file.read()
    return file_text


def merge_files(filename_list, merged_file, encode):
    """
    Merges files in another file from least lines in a file to most

    :param filename_list: list with names of files that needs to be merged
    :param merged_file: file in which text should be written
    :param encode: utf-8 encoding
    :return: nothing
    """
    lines_counter = list()
    for file_name in filename_list:
        lines_counter.append(count_lines(file_name))
    lines_counter.sort(key=lambda item: item[-1])
    with open(merged_file, 'w', encoding=encode) as file:
        for doc in lines_counter:
            file.write(f'{doc[0]}\n')
            file.write(f'{doc[1]}\n')
            text = get_text(doc[0])
            file.write(f'{text}\n\n')


path = 'recipes.txt'
encoding_type = 'utf-8'
mode = 'r'
list_of_dishes = ['Омлет', 'Запеченный картофель']
servings= 3
file_list = ['text_1.txt', 'text_2.txt', 'text_3.txt']
result = 'spliced_text.txt'

cook_book = get_recipes_dict(path, mode, encoding_type)
print(cook_book)
shopping_list = get_shop_list_by_dishes(cook_book, list_of_dishes, servings)
print(shopping_list)
merge_files(file_list, result, encoding_type)
print('Файлы соединены.')



