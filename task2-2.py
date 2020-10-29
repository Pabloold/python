my_list = []
user_count = input('Введите количество элементов в списке ')

if not user_count.isdigit():
    print('Введён неверный формат числа')
    exit()

count = int(user_count)
my_list.append(int(input('Введите первое число списка: ')))

i = 1

while i < count:
    my_list.append(int(input('Введите следующее число списка: ')))
    i += 1

print(my_list)

for a in range(1, len(my_list), 2):
    my_list[a - 1], my_list[a] = my_list[a], my_list[a - 1]

print(my_list)