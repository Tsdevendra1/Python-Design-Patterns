"""
Why: You want an interface for a specific class. This class can vary its behaviour. If you used inheritance from a base class, composing different aspects
of the behaviour you want can get quite messy if the behaviours is in different classes. Bridge pattern simply says, you inject a single class with the desired
implementations you require, but the implementation is hidden behind an interface. To summarise: composition over inheritance

Example: You have a shape class. It has a draw function. This draw function will vary for a shape type (triangle, square etc...) and for a colour (red,
blue, etc...). If you wanted a red triangle, blue triangle, red square, blue square you already have 4 classes you have to implement and perhaps copy and
paste logic. Instead, you have one shape class which takes a colour and shape type in its constructor which implements its own required logic. This way you
can mix and match very easily.
"""
from abc import ABC, abstractmethod


class Color(ABC):

    @abstractmethod
    def draw(self):
        pass


class ShapeType(ABC):

    @abstractmethod
    def draw_shape(self):
        pass


class Red(Color):
    def draw(self):
        pass


class Blue(Color):
    def draw(self):
        pass


class Triangle(ShapeType):
    def draw_shape(self):
        pass


class Square(ShapeType):
    def draw_shape(self):
        pass


class Shape:

    def __init__(self, color: Color, shape_type: ShapeType):
        self.__shape_type = shape_type
        self.__color = color

    def draw(self):
        self.__color.draw()
        self.__shape_type.draw_shape()


def client(shape: Shape):
    shape.draw()


def main():
    red = Red()
    blue = Blue()
    triangle = Triangle()
    square = Square()

    red_triangle = Shape(color=red, shape_type=triangle)
    blue_triangle = Shape(color=blue, shape_type=triangle)
    red_square = Shape(color=red, shape_type=square)
    blue_square = Shape(color=blue, shape_type=square)

    # Client doesn't care about the implementation details
    client(shape=red_triangle)
    client(shape=red_square)
    client(shape=blue_triangle)
    client(shape=blue_square)
