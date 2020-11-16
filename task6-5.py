class Stationery:
    title: str

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с {self.title} ")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} тоже можно отрисовать")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title}ом сложно отрисовывать")


sketch_stationery = Stationery("")
sketch_pen = Pen("Карандаш")
sketch_pencil = Pencil("Ручка")
sketch_handle = Handle("Маркер")

sketch_stationery.draw()
sketch_pen.draw()
sketch_pencil.draw()
sketch_handle.draw()
