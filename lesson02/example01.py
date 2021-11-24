'''
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

# Список с элементами разных Типов
my_list = [2, "Text", 2.0, None, True, [1, 2, 3], (1, 2, 3), {'1': '1', '2': '2'}]

# Перебираем элементы списка по порядку, определяя его Тип
for x in my_list:
    print(f'{x} is {type(x)}')
