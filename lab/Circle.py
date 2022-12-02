from math import pi

class Circle:

    def __init__(self, R, color):
        self.__radius = R
        self.__color = color
        self.__area = pi * R * R

    def __repr__(self):
        return "\
\n\
Круг:\n\
Радиус: {}\n\
Цвет: {}\n\
Площадь: {}\n\
".format(self.__radius, self.__color, self.__area)
