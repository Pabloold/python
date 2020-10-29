'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
'''

my_list = [6, 5, 5, 3, 2, 2, 0]
new_score = int(input('Введите балл: '))
i = 0
for i in range(0, len(my_list), 1):
    if new_score > my_list[i]:
        my_list.insert(i, new_score)
        break
    elif new_score <= my_list[len(my_list)-1]:
        my_list.append(new_score)
        break

print(my_list)
