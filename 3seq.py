str_one=input('Введите элементы первого списка через запятую(,): ')

print(str_one)
list_one=str_one.split(',')
print(list_one)

str_two=input('Введите элементы второго списка через запятую(,): ')
list_two=str_two.split(',')
print(list_two)

list_one=set(list_one)
list_two=set(list_two)

print('Элементы первого списка без тех элементов, которые присутствуют во втором списке: ')
print(list_one-list_two)

print('Элементы второго списка без элементов, которые есть в первом списке')
print(list_two-list_one)

print('Элементы, которые присутствуют в обоих списках: ')
print(list_one&list_two)
