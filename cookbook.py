def get_cook_book():
    cook_book = {}
    with open('book.txt', encoding='utf-8') as recipes:
        for line in recipes:
            key = line.strip()
            num_of_ingrid = recipes.readline().strip()
            ingridient_list = []
            for i in range(int(num_of_ingrid)):
                value = recipes.readline().strip()
                split_value = value.split(' | ')
                ingridient_dict = {'ingridient_name': split_value[0],
                                   'quantity': int(split_value[1]), 'measure': split_value[2]}
                ingridient_list.append(ingridient_dict)
            recipes.readline()
            cook_book[key] = ingridient_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, recipes_dict):
    shop_list = {}
    cook_book = recipes_dict
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_ingridient = dict(ingridient)
            new_shop_list_ingridient['quantity'] *= person_count
            if new_shop_list_ingridient['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_ingridient['ingridient_name']] = new_shop_list_ingridient
            else:
                shop_list[new_shop_list_ingridient['ingridient_name']]['quantity'] += new_shop_list_ingridient['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_ingrid in shop_list.values():
        print(f"{shop_list_ingrid['ingridient_name']} {shop_list_ingrid['quantity']} {shop_list_ingrid['measure']}")


def get_person_count():
    return int(input('Введите количество персон: '))


def input_dishes():
    dishes = input('Введите названия блюд через запятую на одного человека: ').split(', ')
    return [dish.capitalize() for dish in dishes]


if __name__ == '__main__':
    print_shop_list(get_shop_list_by_dishes(input_dishes(), get_person_count(), get_cook_book()))