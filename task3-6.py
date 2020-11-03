string = input('Введите строку для преобразования: ').split()
fin_string = []


def int_func(a):
    return a.capitalize()


for el in string:
    fin_string.append(int_func(el))

print(' '.join(fin_string))
