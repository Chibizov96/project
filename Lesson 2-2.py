# Задание-2: Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
number = int(input('Введите количетсов элементов: '))
i=0
my_list=[]
while i < number:
    el=input("Введите элемент списка: ")
    my_list.append(el)
    i+=1
if len(my_list) % 2 == 0:
    i = 0
    while i< len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i] = el
    i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)
