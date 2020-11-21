class Clothes():
    def __init__(self, attrs: int):
        self.value = attrs

    def calc_fabric(self):
        print("Расчет расхода ткани")


class Coat(Clothes):
    @property
    def calc_fabric(self, ):
        return self.value / 6.5 + 0.5


class Costume(Clothes):
    @property
    def calc_fabric(self):
        return 2 * self.value + 0.3


class CalcTotal(Clothes):
    def __init__(self, attrs: int, attrs2: int):
        super().__init__(attrs)
        self.value = attrs
        self.value2 = attrs2

    @property
    def calc_fabric(self):
        return self.value / 6.5 + 0.5 + 2 * self.value2 + 0.3


size, height = 48, 5

obj_coat = Coat(size)
obj_costume = Costume(height)
obj_total = CalcTotal(size, height)

print(f"Расход ткани для пальто  >>> {obj_coat.calc_fabric:.2f}")
print(f"Расход ткани для костюма >>> {obj_costume.calc_fabric:.2f}")
print(f"Общий расход ткани  >>> {obj_total.calc_fabric:.2f}")
