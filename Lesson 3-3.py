'''Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''
def my_func(x, y, z):
    initial = [x, y, z]
    finish = []
    max_1 = max(initial)
    finish.append(max_1)
    initial.remove(max_1)
    max_2 = max(initial)
    finish.append(max_2)
    print(sum(finish))

my_func(2, 3, 7)