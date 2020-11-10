import json

new_dict, profit_dict, average_dict, loss_dict = {}, {}, {}, {}
profit, average_profit, count = 0, 0, 0

with open('for_task6.txt') as file:
    for line in file.readlines():
        name, type_of_firm, revenue, costs = line.split()
        new_dict[name] = int(revenue) - int(costs)
        if new_dict.get(name) > 0:
            average_profit += new_dict.get(name)
            profit_dict[name] = new_dict.get(name)
            count += 1
        else:
            loss_dict[name] = new_dict.get(name)
    average_profit /= count
    average_dict["average_profit"] = round(average_profit)
    firm_list = [profit_dict, average_dict, loss_dict]
    print(
        f'Фирмы с прибылью: {profit_dict}\nСредняя прибыль: {average_dict.get("average_profit")}\n'
        f'Фирмы с убытком: {loss_dict}')

with open('list.json', 'w') as json_file:
    json.dump(firm_list, json_file)
    json_string = json.dumps(firm_list)
    print(f'Содержание файла list.json: {json_string}')
