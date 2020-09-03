"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * (ширина) * (масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см) * число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    __length = None
    __width = None  # ширина
    weigth = None
    thickness = None  # толщина

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.weigth = 25
        self.thickness = 0.05    # это 5 см

    def building(self):
        building = self.length * self.width * self.weigth * self.thickness / 1000
        print("Итого: ", building, "тонн")


road = Road(20, 5000)
road.building()
