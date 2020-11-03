div1 = input('Введите делимое >>> ')
div2 = input('Введите делитель >>> ')


def division(a, b):
    try:
        c = float(a) / float(b)
        return f'{c:.04f}'
    except ZeroDivisionError:
        return f'{a}/{b}=infinite'
        # так и не нашел как вывыести символ бесконечности с помощью chr() вместо infinite
    except ValueError:
        return 'Делим цифры а не буквы!'


print(division(div1, div2))
