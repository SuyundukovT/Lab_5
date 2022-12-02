class Color:

    def __init__(self, R, G, B):
        self.__color = R+G+B

    def __repr__(self):
        return self.__color