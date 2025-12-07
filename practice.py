#-*- coding: utf-8 -*-

#Включение словаря с помощью range()
my_dict= {}
key = 0

for item in range(10):
    my_dict[key] = item ** 2
    key += 1
print(type(my_dict), my_dict)
#Или так -
my_dict = {key: key*key for key in range(10)}
print(type(my_dict), my_dict)

#Включение списка с помощью range()
my_list = [num for num in range(10) if num % 2 != 0]
print(type(my_list), my_list)

#Включение множества с помощью range()
my_set = {even for even in range(10) if even % 2 == 0}
print(type(my_set), my_set)

#Включение генератора спомощью range()
my_range = (tup for tup in range(10) if tup % 2 != 0)
for i in my_range:
    print(i)
print(type(my_range))

#Создание кортежа
my_tuple = tuple(range(10))
print(type(my_tuple), my_tuple)

