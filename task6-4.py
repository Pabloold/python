from time import sleep


class Car:
    speed = 0
    name: str
    color: str
    max_speed: int
    direction: str
    is_police: bool

    def __init__(self, name, color, max_speed=80, direction='straight', is_police=False):
        self.name = name
        self.color = color
        self.max_speed = max_speed
        self.direction = direction
        self.is_police = is_police

    def show_speed(self):
        print(f'Current speed > {self.speed}')

    def go(self):
        print(f'Car - {self.name}, color - {self.color}')
        print('Starting engine')
        self.show_speed()
        sleep(1.5)
        while self.speed < self.max_speed:
            self.speed += 10
            self.show_speed()
            sleep(1.5)
        print(f'MAX SPEED!! {self.speed}')

    def turn(self):
        print(f'Turn {self.direction}')
        sleep(1)

    def stop(self):
        print('Stopping >>>')
        while self.speed > 0:
            self.speed -= 20
            self.show_speed()
            sleep(0.5)
        print('STOPPED!!')
        sleep(1.5)


class TownCar(Car):

    def show_speed(self):
        print(f'Current speed > {self.speed}')
        if self.speed > 60:
            print('SLOW DOWN!!')


class WorkCar(Car):

    def show_speed(self):
        print(f'Current speed > {self.speed}')
        if self.speed > 40:
            print('SLOW DOWN!!')


class PoliceCar(Car):
    def __init__(self, name, color, max_speed, direction):
        super().__init__(name, color, max_speed, direction)
        self.is_police = True

    def go(self):
        print(f"Car - {self.name}, color - {self.color}. It's a POLICE CAR!")
        print('Starting engine!')
        self.show_speed()
        sleep(0.6)
        while self.speed < self.max_speed:
            self.speed += 10
            self.show_speed()
            sleep(0.6)
        print(f'MAX SPEED!! {self.speed}')


class SportCar(Car):
    def go(self):
        print(f'Car - {self.name}, color - {self.color}')
        print('Starting engine')
        self.show_speed()
        sleep(0.4)
        while self.speed < self.max_speed:
            self.speed += 10
            self.show_speed()
            sleep(0.4)
        print(f'MAX SPEED!! {self.speed}')

    def stop(self):
        print('Stopping >>>')
        while self.speed > 0:
            self.speed -= 20
            self.show_speed()
            sleep(0.25)
        print('STOPPED!!')


town_car = TownCar('GAZ', 'BLACK', 80, 'LEFT')
town_car.go()
town_car.turn()
town_car.stop()

work_car = WorkCar('MAZ', 'RED', 60, 'LEFT')
work_car.go()
work_car.turn()
work_car.stop()

police_car = PoliceCar('LADA', 'WHITE', 180, 'RIGHT')
police_car.go()
police_car.turn()
police_car.stop()

sport_car = SportCar('BUGATTI', 'SILVER', 220, 'RIGHT')
sport_car.go()
sport_car.turn()
sport_car.stop()
