from graphics import *
import math

class CButton:
    def __init__(self, win, center, radius, label):
        self.center = center
        self.radius = radius
        self.circle = Circle(center, radius)
        self.circle.setFill("lightgray")
        self.circle.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def get_label(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill("black")
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill("darkgrey")
        self.circle.setWidth(1)
        self.active = False

    def get_distance(self, p):
        self.distance = math.sqrt((p.getX() - self.center.getX())**2 + (p.getY() - self.center.getY())**2)

    def clicked(self):
        return (self.active and 
                self.distance <= self.radius)