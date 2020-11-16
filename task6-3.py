class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        print(
            f'Worker: {self.get_full_name()} - {self.position} - Wage: '
            f'{self._income.get("wage") + self._income.get("bonus")}')


example = Position('John', 'Dow', 'Manager', {"wage": 65000, "bonus": 15000})
example.get_total_income()
