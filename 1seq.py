number_of_elements = int(input('Задайте количество элементов в списке: '))

list_all = []

i = 0
while i < number_of_elements:
    list_all.append(int(input(f'Введите значение элемента {i + 1}: ')))
    i += 1

print(list_all)
print(type(list_all))

