class NumberCell:
    def __init__(self, number_x: int):
        self.number_x = number_x

    def __add__(self, other):
        return f"Сложение, размер клетки равен >>> {self.number_x + other.number_x}"

    def __sub__(self, other):
        return f"Вычитание, размер клетки равен >>> {self.number_x - other.number_x}" \
            if self.number_x - other.number_x > 0 else "Клетка исчезла"

    def __mul__(self, other):
        return f"Умножение, размер клетки равен >>> {self.number_x * other.number_x}"

    def __truediv__(self, other):
        return f"Деление, размер клетки равен >>> {self.number_x // other.number_x}"

    def make_order(self, cell_row):
        row_cell = ''
        for i in range(int(self.number_x / cell_row)):
            row_cell += '*' * cell_row + '\n'
        row_cell += '*' * (self.number_x % cell_row)
        return row_cell


cell_base = NumberCell(19)
cell_change = NumberCell(7)

print(cell_base + cell_change)
print(cell_base - cell_change)
print(cell_base * cell_change)
print(cell_base / cell_change)

print(f"Метод make_order() позволяет организовать ячейки по рядам:")
print(cell_base.make_order(5))
