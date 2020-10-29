season_list = ['зима', 'весна', 'лето', 'осень']
season_dic = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}

user_month = int(input('Введите номер месяца '))

if 0 < user_month < 3 or user_month == 12:
    print(season_list[0])
    print(season_dic.get(1))
elif 2 < user_month < 6:
    print(season_list[1])
    print(season_dic.get(2))
elif 5 < user_month < 9:
    print(season_list[2])
    print(season_dic.get(3))
elif 8 < user_month < 12:
    print(season_list[3])
    print(season_dic.get(4))
else:
    print('В году 12 месяцев, а не', user_month)
