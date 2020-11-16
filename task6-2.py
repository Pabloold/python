class Road:
    _length: int
    _width: int

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def calculation(self):
        result = self._length * self._width * 25 * 5 / 1000
        print(f'Масса асфальта, необходимая для покрытия всего дорожного полотна {result:.0f} т.')


mass = Road(20, 5000)
mass.calculation()
