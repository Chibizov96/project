"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:
    speed = 50
    color = "White"
    name = "BMW"
    is_police = False

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        self.direction = direction
        if direction.lower() == "направо":
            print("Машина повернула направо")
        else:
            print("Машина повернула налево")

    def show_speed(self):
        print(self.speed)

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Вы превышаете скорость")

class SportCar(Car):

    def go(self):
        print("Поехали")

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Вы превышаете скорость")

class PoliceCar(Car):

    def show_speed(self):
        if self.speed > 80:
            print("Вы превышаете скорость")

print(Car.speed)
a = TownCar()
b = SportCar()
c = WorkCar()
d = PoliceCar()
a.turn("Налево")
b.stop()
c.show_speed()
d.go()