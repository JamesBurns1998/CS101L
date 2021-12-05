#############################################################################################################
## James Burns
## CS101 Lab
## Assignment 12
##
## PROBLEM: Create a program which contains four classes: a parent class "Point" which uses turtle module to draw a point; A "Box" class which inherits "Point" class and draws a rectangle using turtle; a "BoxFilled" class which inherits Box and draws a box with filled color; A Circle class which inherits Point and draws a circle with a given radius; and a CircleFilled Class which inherits circle and draws a filled circle. 
##
## ALGORITHM:
##  1.  import turtle module
##  2.  Create a class "Point" with parameters x, y, and color
##  3.  Define class methods for Point class: draw() and draw_action()
##  4.  Create a class "Box" which inherits Point and has parameters x, y, width, height, color
##  5.  Define class mehtod for Box class: draw_action() to draw a box using turtle
##  6.  Create a class "BoxFilled" which inherits Box and has parameters x, y, width, height, color, fill_color
##  7.  Define class method for BoxFilled: draw_action() which calls Box.draw_action() and fills box with self.fill_color
##  8.  Create a class "Circle" which inherits Point and has parameters x, y, radius, color
##  9.  Define class method for Circle: draw_action() which uses turtle to draw a circle radius self.radius
##  10. Create a class "CircleFill" which inherits Circle and has parameters x, y, radius, circle, fill_color
##  11. Define class method for CircleFIll: draw_action() which calls Circle.draw_action() and fills circle with self.fill_color
## In Main:
##  12. Create an instance of Point(), p. Call class method draw() for p
##  13. Create an instance of Box(), b. Call class method draw() for b
##  14. Create an instance of BoxFilled(), bf. Call class method draw() for bf
##  15. Create an instance of Circle(), c. Call class method draw() for c
##  16. Create an instance of CircleFilled(), cf. Call class method draw() for cf
##
######################################################################################################################


import turtle

class Point(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    def draw_action(self):
        turtle.dot()

class Box(Point):

    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color)
        self.width = width
        self.height = height
    
    def draw_action(self):
        for turn in range(2):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)
    

class BoxFilled(Box):
    def __init__(self, x, y, width, height, color, fill_color):
        super().__init__(x, y, width, height, color)
        self.fill_color = fill_color
    
    def draw_action(self):
        turtle.fillcolor(self.fill_color)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius
    
    def draw_action(self):
        turtle.circle(self.radius)


class CircleFilled(Circle):
    def __init__(self, x, y, radius, color, fill_color):
        super().__init__(x, y, radius, color)
        self.fill_color = fill_color
    
    def draw_action(self):
        turtle.fillcolor(self.fill_color)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()

if __name__ == "__main__":
    p = Point(-100,100,"red")
    p.draw()

    b = Box(120,120,70,50,"blue")
    b.draw()

    bf = BoxFilled(30,30,50,80,"red","yellow")
    bf.draw()

    c = Circle(20,20,7,"black")
    c.draw()

    cf = CircleFilled(80,80,10,"green","red")
    cf.draw()