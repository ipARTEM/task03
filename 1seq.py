text = 'Задайте количество элементов в списке от 1 до 100: '

list_new = []
answer_int = None

while True:
    answer = input(text)
    try:
        answer_int = int(answer)
        if 0 < answer_int < 101:
            list_new = [answer_int - 1]
            print(f'Список на {answer_int} элементов создан')
        break

    except:
        pass

print(list_new)
print(answer_int)

for i in range(answer_int):
    answer_element = input(f'Введите значение элемента {i + 1}: ')
    list_new[i] = answer_element

print(list_new)
