from time import sleep


class TrafficLight:
    __color_check = ['красный', 'желтый', 'зелёный']
    color_list: list
    timer_list: list

    def __init__(self, color, timing):
        self.color_list = color
        self.timer_list = timing

    def running(self):
        for i in range(len(self.color_list)):
            if self.color_list[i] == self.__color_check[i]:
                print(f'Горит {self.color_list[i]}')
                sleep(self.timer_list[i])
            else:
                print('Нарушен порядок цветов!')
                break


tr_color = TrafficLight(['красный', 'желтый', 'зелёный'], [7, 2, 5])
tr_color.running()
print('При нарушении порядка цветов выходит соответствующее сообщение')
sleep(1)
tr_color = TrafficLight(['красный', 'зелёный', 'желтый'], [7, 2, 5])
tr_color.running()
