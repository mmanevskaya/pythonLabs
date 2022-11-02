from color import *
from math import *


class Circle:

    name = 'Круг'

    def __init__(self, radius, color):
        self.color = Color(color)
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def repr(self):
        return f'''Радиус: {self.radius}
                    Цвет: {self.color.get_color()}
                    Площадь: {self.area()}
                    '''

    def get_name(self):
        return self.name