list_all = input('Введите любые числа через запятую: ')

list_new = list_all.split(',')

print(list_new)
print(type(list_new))

set_new = set(list_new)
print(set_new)


def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str


replace_values = {';': ',', '/': ','}

list_all = input('Введите любые числа через запятую(,),точку с запятой(;), слеш(/): ')


def finish_text(text):
    text_new = multiple_replace(text, replace_values)
    text_str = text_new.split(',')
    text_list = list(text_str)
    return text_list


list_new = finish_text(list_all)

print(list_new)
