from sys import argv

file_name, worker_hour, rate, benefit = argv
try:
    calculation = float(worker_hour) * float(rate) + float(benefit)
except ValueError:
    print('ValueError')

try:
    print(f'К выплате: {calculation}')
except NameError:
    print('NameError')
