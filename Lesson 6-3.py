"""
Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    name = ""
    lastname = ""
    position = ""
    _income = {}

class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя сотрудника {self.name}, {self.lastname}")

    def get_total_income(self):
        print(f"Зарплата сотрудника {self._income['wage'] + self._income['bonus']}")

a = Position()
a.name = "Yakov"
a.lastname = "Chibizov"
a._income = {"wage": 30000, "bonus": 10000}
a.get_full_name()
a.get_total_income()