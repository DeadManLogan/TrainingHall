from graphics import *
from practice import Projectile
from button import Button

class ShotTracker:
    def __init__(self, win, angle, velocity, height):
        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)
        self.max_height = height

    def update(self, dt):
        self.proj.update(dt)
        center = self.marker.getCenter()
        dx = self.proj.get_x() - center.getX()
        dy = self.proj.get_y() - center.getY()
        self.marker.move(dx, dy)

        if self.proj.get_y() > self.max_height:
            self.max_height = self.proj.get_y()
    
    def get_x(self):
        return self.proj.get_x()
    
    def get_y(self):
        return self.proj.get_y()
    
    def get_max_height(self):
        return self.max_height
    
    def undraw(self):
        return self.marker.undraw()
    
class InputDialog:
    def __init__(self, angle, vel, height):
        self.win = win = GraphWin("Initial Values", 200, 300)
        win.setCoords(0, 4.5, 4, 0.5)

        Text(Point(1, 1), "Angle").draw(win)
        self.angle = Entry(Point(3, 1), 5).draw(win)
        self.angle.setText(str(angle))

        Text(Point(1, 2), "Velocity").draw(win)
        self.vel = Entry(Point(3, 2), 5).draw(win)
        self.vel.setText(str(vel))

        Text(Point(1, 3), "Height").draw(win)
        self.height = Entry(Point(3, 3), 5).draw(win)
        self.height.setText(str(height))

        self.fire = Button(win, Point(1, 4), 1.25, 0.5, "Fire!")
        self.fire.activate()

        self.quit = Button(win, Point(3, 4), 1.25, 0.5, "Quit")
        self.quit.activate()

    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"
    
    def get_values(self):
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        h = float(self.height.getText())
        return a, v, h
    
    def close(self):
        self.win.close()
        

def main():
    win = GraphWin("Projectile Animation", 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)

    Line(Point(-10, 0), Point(210, 0)).draw(win)

    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)

    angle, vel, height = 45, 40, 2
    while True:
        inputwin = InputDialog(angle, vel, height)
        choice = inputwin.interact()
        inputwin.close()

        if choice == "Quit":
            break

        angle, vel, height = inputwin.get_values()
        shot = ShotTracker(win, angle, vel, height)

        while 0 <= shot.get_y() and -10 < shot.get_x() <= 210:
            shot.update(1/50)
            update(50)
    win.close()

main()