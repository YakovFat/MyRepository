cook_book = {}
ingredients = []
with open('recipe_book.txt') as f:
    for line in f:
        name = line.strip()
        number = f.readline().strip()
        for ing in range(int(number)):
            ing = f.readline().strip()
            ing_list = []
            ing_list.append(ing.split(' | '))
            ing_dict = {'ingridient_name': ing_list[0][0], 'quantity': int(ing_list[0][1]), 'measure': ing_list[0][2]}
            ingredients.append(ing_dict)
        cook_book[name] = ingredients
        ingredients = []
        f.readline()
    print(cook_book, '\n' * 3)


def get_shop_list_by_dishes(dishes, person_count):
    dish_user = {}
    for dish in dishes:
        if dish in cook_book:
            for i in cook_book[dish]:
                dish_key = i['ingridient_name']
                dish_user[dish_key] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
    print(dish_user)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
