# Создать список и заполнить его элементами различных типов данных.
# # Реализовать скрипт проверки типа данных каждого элемента.
# # Использовать функцию type() для проверки типа.
# # Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
some_int = 5
some_float = 1.3
some_str = "Hello"
some_list = ['a', '1']
some_tuple = ('b', '2')
some_dict = {'city': 'Ryazan', 'country': 'Russia', 'age':'23', 'Name':'Yakov'}
super_list = [some_int, some_float, some_str, some_list, some_tuple, some_dict]
for i in super_list:
    print(f'{i} is {type(i)}')