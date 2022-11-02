from rectangle import *


class Square(Rectangle):

    name = 'Квадрат'

    def __init__(self, width, color):
        self.color = Color(color)
        self.width = width
        self.height = width

    def repr(self):
        return f'''Длина стороны: {self.width}
                    Цвет: {self.color.get_color()}
                    Площадь: {self.area()}
                    '''

    def get_name(self):
        return self.name
