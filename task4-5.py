from functools import reduce

my_list = [num for num in range(100, 1001) if num % 2 == 0]
print(my_list)
print(reduce(lambda total, amount: total * amount, my_list))
