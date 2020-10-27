# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

goods = []
while input("Вы хотите добавить продукт? Введите да/нет ") == 'да':
    number = int(input("Введите номер продукта: "))
    features = {}
    feature_key = 'название'
    feature_value = input("Введите название: ")
    features[feature_key] = feature_value
    feature_key = 'цена'
    feature_value = input("Введите цену: ")
    features[feature_key] = feature_value
    feature_key = 'количество'
    feature_value = input("Введите количество: ")
    features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
#goods = [(1, {'name': 'comp', 'price': '11'}), (2, {'name': 'pri', 'price': '22'})]
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)