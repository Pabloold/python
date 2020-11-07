from itertools import count, cycle


def func_cel_numbers(start, stop):
    for cel_numbers in count(start):
        if cel_numbers > stop:
            break
        print(cel_numbers)


def func_my_cycle(my_list, repeat):
    my_count = 0
    for my_cycle in cycle(my_list):
        if my_count == repeat:
            break
        print(my_cycle)
        my_count += 1


try:
    func_cel_numbers(start=int(input('Введите начальное число ')), stop=int(input('Введите последнее число ')))
    func_my_cycle(my_list=[1, 2, 3, 4], repeat=int(input('Введите колличество проходов ')))
except ValueError:
    print('ValueError')
