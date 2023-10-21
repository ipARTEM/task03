

list_test=['авто', 'велосипед','самокат','мотоцикл','автобус']
print(type(list_test))
#1
list_test.append('грузовик')
print(list_test)

#2
list_test.sort()
print(list_test)
#3
list_test.reverse()
print(list_test)

#4
list_test.insert(2,'трактор')
print(list_test)

#5
list_test.remove('самокат')
print(list_test)

#6
list_test.clear()
print(list_test)

dict_test={'name':'Alice','age':23, }
print(type(dict_test))
#1
dict_copy=dict_test.copy()
print(dict_copy)
print(dict_test)

#2
print(dict_copy.clear())

#3
print(dict_test.keys())

#4
print(dict_test['age'])

#5
print(dict_test.get('name'))

set_test={'яблоко', 'банан','вишня','ананас'}
print(type(set_test))
print(set_test)

#1
set_new=set_test.copy()
set_new.add('киви')
print(set_test)

#2
set_new.remove('вишня')
set_new.remove('ананас')
print(set_new)
print(set_test)
#3
print(set_test|set_new)

#4
print(set_test&set_new)

#5
print(set_test-set_new)
print(set_new-set_test)

str_test='Тестирование основных методов со строкой'
print(str_test)
print(type(str_test))

#1
print(str_test.upper())
#2
print(str_test.lower())

#3
print(str_test.count('т'))

#4
print(str_test.replace('Тестирование', 'Проверка'))

#5
print(str_test.find('основных'))




