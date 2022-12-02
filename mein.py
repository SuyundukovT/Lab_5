from lab.Circle import *
from lab.Rectangle import *
from lab.Color import *





def main():
    rectangle = Rectangle(Color("11","22","31"), 10, 20)
    print(rectangle)
    circle = Circle(8, Color("12","34","96"))
    print(circle)
    square = Square(Color("25", "67", "58"), 10)
    print(square)

if __name__ == '__main__':
    main()