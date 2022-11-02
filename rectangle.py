from color import *


class Rectangle:

    name = 'Прямоугольник'

    def __init__(self, width, height, color):
        self.color = Color(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def repr(self):
        return f'''Ширина: {self.width}
                    Высота: {self.height}
                    Цвет: {self.color.get_color()}
                    Площадь: {self.area()}
                    '''

    def get_name(self):
        return self.name

