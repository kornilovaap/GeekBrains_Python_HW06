'''
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    title = None

    def draw(self):
        print("1) Запуск отрисовки.")


class Pen (Stationery):
    def draw(self):
        print("2) Отрисовка запущена.")


class Pencil (Stationery):
    def draw(self):
        print("3) В процессе отрисовки.")


class Handle (Stationery):
    def draw(self):
        print("4) Отрисовка завершена.")


my_stationery = Stationery()
my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_stationery.draw()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
