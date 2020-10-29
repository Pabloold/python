my_str = input("Введите строку: ")
a = my_str.split(' ')
for el in a:
    if len(el) > 10:
        el = el[0:10]
    print(el)
