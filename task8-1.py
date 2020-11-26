class Date:
    date: str

    def __init__(self, date: str = 'dd-mm-yyyy'):
        self.date = date

    @classmethod
    def date_get(cls, date):
        try:
            return [int(el) for el in date.split('-')]
        except ValueError:
            print("Wrong date")
            exit()

    @staticmethod
    def date_validate(date: list):
        day, month, year = date
        if 0 < day < 32 and 0 < month < 13:
            return f'Date {day:02d}:{month:02d}:{year:0004d} is correct'
        else:
            return f'Date {day:02d}:{month:02d}:{year:0004d} incorrect'


user_date = input('Type date in format dd-mm-yyyy >>> ')
val_date = Date.date_get(user_date)
print(Date.date_validate(val_date))
