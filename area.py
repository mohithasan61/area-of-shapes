
import math
from turtle import circle


def about_shape(shape, data, area):
    print(f"About the shape :\nShape : {shape}\n{data}\narea = {area}")

class Triangle:
    base, height = int(), int()

    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        data = f"base = {self.base}\nheight = {self.height}"
        about_shape("Triangle", (data), ((self.base)*(self.height)*(1/2)))

class Rectangle:
    base, height = int(), int()

    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        data = f"base = {self.base}\nheight = {self.height}"
        about_shape("Rectangle", (data), ((self.base)*(self.height)))

class Square:
    hand = int()

    def __init__(self, hand):
        self.hand = hand
    
    def area(self):
        data = f"hand = {self.hand}"
        about_shape("Square", (data), ((self.hand)**2))

class Circle:
    radius = int()

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        data = f"hand = {self.radius}"
        about_shape("Circle", (data), ((math.pi)*((self.radius)**2)))

def triangle():
    a = int(input("base = "))
    b = int(input("height = "))
    triangle = Triangle(a, b)
    print("----------")
    triangle.area()
def square():
    a = int(input("hand = "))
    square = Square(a)
    print("----------")
    square.area()
def rectangle():
    a = int(input("base = "))
    b = int(input("height = "))
    rectangle = Rectangle(a, b)
    print("----------")
    rectangle.area()
def circle():
    a = int(input("radius = "))
    circle = Circle(a)
    print("----------")
    circle.area()

while 5==5:
    shapes = {"Square" : 1, "Rectangle" : 2, "Circle" : 3, "Triangle" : 4}
    print(shapes)
    shape = int(input())
    if (shape == 1):
        square()
    elif (shape == 2):
        rectangle()
    elif (shape == 3):
        circle()
    elif (shape == 4):
        triangle()
