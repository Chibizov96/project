'''Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''
result = 0
while True:
    line = input("Введите числа через пробел, q для выхода: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'q':
                print(f"Ваша сумма {result}.")
                exit(0)
            else:
                print(f"Ваша сумма {result}. Ошибка ввода")
                exit(1)