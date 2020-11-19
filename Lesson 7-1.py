"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""

class ShMatrix:
    _length_x = 0 # максимальная длина по x
    _length_y = 0 # максимальная длина по y
    def __init__(self, matrix:list):
        self._length_x = len(matrix[0])    # количество элементов в одной строке матрицы
        self._length_y = len(matrix)       # количество строк в матрице
        if not isinstance(matrix, list):
            raise Exception('Неверная инициализация матрицы! В список должен передаваться список значений типа "int"')
        for index, items in enumerate(matrix, 1):
            if not isinstance(items, list):
                raise Exception(
                        'Неверная инициализация матрицы! В список должен передаваться список значений типа "int"')
            if not len(items) == self._length_x:
                raise Exception(f'Неверное количество элементов в строке №{index}')
            for item in items:
                    if not isinstance(item, int):
                        raise Exception(
                            'Неверная инициализация матрицы! Все значения вложенных списков должны быть типа "int"')
            self.matrix = matrix

            # проверка на совместимость 2х матриц

    def __check_matrix (self, other):
            if not isinstance(other, ShMatrix):
                raise TypeError('Неверный тип аргумента.')
            if self._length_x != other._length_x:
                raise TypeError('Ошибка. Разная длина строк у аргументов.')
            if self._length_y != other._length_y:
                raise TypeError('Ошибка. Разная длина столбцов у аргументов.')

    def __str__(self):
            # здесь все просто. выводим построчно
            # я не стал ничего выдумывать, а воспользовался тем что вывод списка или кортежа будет приемлемо выглядеть
            st = ''
            for items in self.matrix:
                st += str(items) + '\n'
                return st

                # @__check_matrix(other) # я видимо еще не до конца понял как работают декораторы, буду рад подсказке

    def __add__(self, other):
                self.__check_matrix(other)
                res = []  # итак, нам нужен пустой список куда будем сохранять данные
                for mrx1, mrx2 in zip(self.matrix, other.matrix):
                    res.append(list(map(sum, zip(mrx1, mrx2))))
                return ShMatrix(res)

a = ShMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Matrix a:')
print(a)

print('Matrix b:')
b = ShMatrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(b)

c = a + b
print('Matrix c:')
print(c)