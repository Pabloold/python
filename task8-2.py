class MyZeroDiv(Exception):
    def __init__(self, divided, divider):
        self.divided = divided
        self.divider = divider

    def __str__(self):
        return "Can't divide on Zero"


def dividing(div1, div2):
    if div2 == 0:
        raise MyZeroDiv(user_divided, user_divider)
    else:
        return div1 / div2


try:
    user_divided = float(input("Insert divided >> "))
    user_divider = float(input("Insert divider >> "))
    try:
        c = dividing(user_divided, user_divider)
        print(f'Result >>> {c:.01f}')
    except MyZeroDiv as exception:
        print("Can't divide on Zero")
except ValueError:
    print('Wrong format')
