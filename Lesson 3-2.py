'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''

def my_func(name, surname, byear, city, email, phone):
    print(name, surname, byear, city, email, phone)

my_func(name= 'Yakov', surname='Chibizov', byear=1996, city='Ryazan', email='chibizov96@gmail.com', phone='1-234-567-89-00')