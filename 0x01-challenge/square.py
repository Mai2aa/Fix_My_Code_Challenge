#!/usr/bin/python3
"""creating  class called a square"""


class Square:
    """ a class with 3 methids inside it """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_my_square(self):
        """ Permiter of my square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ print the width by height """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())

