"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
    для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
    реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod
from math import ceil


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

    @property
    @abstractmethod
    def get_name(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.__size = size

    @property
    def get_name(self):
        return self.name

    @property
    def consumption(self):
        return round(self.__size / 6.5 + 0.5, 2)

    @property
    def get_size(self):
        return self.__size


class Suit(Clothes):
    def __init__(self, name, height):
        self.name = name
        self.__height = height

    @property
    def get_name(self):
        return self.name

    @property
    def consumption(self):
        return round(2 * self.__height + 0.3, 2)  # берём с запасом :-)

    @property
    def get_height(self):
        return self.__height


if __name__ == '__main__':
    coat1 = Coat('Пальто', 54)
    print(f'Вы заказали "{coat1.get_name}", {coat1.get_size}-го размера.')
    print(f'Для его производства понаддобится {coat1.consumption} м. ткани.\n')

    suit1 = Suit('Костюм', 185)
    print(f'Вы заказали "{suit1.get_name}", ваш рост: {suit1.get_height} см.')
    print(f'Для его производства понаддобится {suit1.consumption} см. ткани.\n')
