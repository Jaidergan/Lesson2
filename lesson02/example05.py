"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""
# Задаем список "Рейтинг" и выводит его пользователю
my_list = [8, 6, 6, 4, 1]
print("Рейтинг:", my_list)

# Запрашиваем у пользователя новый элемент рейтинга
number = int(input("Введите новый элемент рейтинга >>> "))

# Проверяем количество элементов, которые соответвуют введеному пользователем
repeats = my_list.count(number)

# Добавляем новый элемент в наш "Рейтинг".
# Если встречается такой(ие) элемент(ы) в списке, то после него/них.
# Если такого элемента в списке еще нет, то добавляет его.
for element in my_list:
    if repeats > 0:
        i = my_list.index(number)
        my_list.insert(i + repeats, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)

# Выводим результат
print("Рейтинг:", my_list)
