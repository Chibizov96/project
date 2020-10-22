#task 1
a = int(input("Введите число для вывода на экран :"))
print(a)

#task 2
b = int(input("Введите время в секундах: "))
hour = b // 3600
minutes = (b - hour *3600) // 60
seconds = b - hour * 3600 - minutes * 60
print(str(hour) + ":" + str(minutes) + ":" + str(seconds))

#task 3
c=input("Введите число N: ")
sum_2=c+c
sum_3=c+c+c
print(int(c) + int(sum_2) + int(sum_3))

#task 4
d=int(input("Введите целое положительное число: "))
m = d % 10
d = d // 10
while d > 0:
    if d % 10 > m:
        m = d % 10
    d = d // 10
print(m)

#task 5
value=int(input("Введите выручку фирмы: "))
tax=int(input("Введите издержки фирмы: "))
if value>tax:
    personal=int(input("Введите количество сотрудников: "))
    print("Рентабельность равна: " + str(round((value/tax), 2)))
    print("Прибыль на сотрудника равна: " + str(value/personal))
else:
    print("Фирма нерентабельна")

#task 6
distance=int(input("Введите дистанцию первого забега, в км: "))
record=int(input("Введите дистанцию, которой хотите достигнуть: "))
day = 0
while distance < record:
    distance=distance*1.1
    day=day+1
print("Потребуется " + str(day))
