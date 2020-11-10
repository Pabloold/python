with open('test.txt') as file:
    string_number = file.readlines()
    print(f'Колличество строк в файле - {len(string_number)}')
    file.seek(0, 0)
    for i in range(len(string_number)):
        words_in_string = file.readline()
        print(f'Слов в строке {i + 1} - {len(words_in_string.split())}.')
