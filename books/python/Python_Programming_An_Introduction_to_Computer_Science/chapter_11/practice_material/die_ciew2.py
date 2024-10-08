from chapter_11.practice_material.graphics import *

class DieView:
    def __init__(self, win, center, size):
        self.win = win
        self.background = "white"
        self.foreground = "black"
        self.psize = 0.1 * size
        hsize = size / 2.0
        offset = 0.6 * hsize

        cx, cy = center.getX(), center.getY()
        p1 = Point(cx - offset, cy - offset)
        p2 = Point(cx + offset, cy + offset)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        self.pips = [self.__make_pip(cx - offset, cy - offset),
                     self.__make_pip(cx - offset, cy),
                     self.__make_pip(cx - offset, cy + offset),
                     self.__make_pip(cx, cy),
                     self.__make_pip(cx + offset, cy + offset),
                     self.__make_pip(cx + offset, cy),
                     self.__make_pip(cx + offset, cy - offset)]
        
        self.on_table = [[], [3], [2, 4], [2, 3, 4], [0, 2, 4, 6], 
                         [0, 2, 3, 4, 6], [0, 1, 2, 4, 5, 6]]
        
        self.set_value(1)

    def __make_pip(self, x, y):
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip
    
    def set_value(self, value):
        for pip in self.pips:
            pip.setFill(self.background)

        for i in self.on_table[value]:
            self.pips[i].setFill(self.foreground)
