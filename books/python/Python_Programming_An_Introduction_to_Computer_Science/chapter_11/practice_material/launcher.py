from math import *
from graphics import *
from cannon import ShotTracker

class Launcher:
    def __init__(self, win):
        base = Circle(Point(0, 0), 3)
        base.setFill("red")
        base.setOutline("red")
        base.draw(win)

        self.win = win
        self.angle = radians(45.0)
        self.vel = 40.0

        self.arrow = Line(Point(0, 0), Point(0, 0)).draw(win)
        self.redraw()
    
    def adj_angle(self, amt):
        self.angle += radians(amt)
        self.redraw()

    def adj_velocity(self, amt):
        self.vel += amt
        self.redraw()
    
    def redraw(self):
        self.arrow.undraw()
        pt2 = Point(self.vel * cos(self.angle), self.vel * sin(self.angle))
        self.arrow = Line(Point(0, 0), pt2).draw(self.win)
        self.arrow.setArrow("last")
        self.arrow.setWidth(3)

    def  fire(self):
        return ShotTracker(self.win, degrees(self.angle), self.vel, 0.0)

class ProjectileApp:
    def __init__(self):
        self.win = GraphWin("Projectile Animation", 640, 480)
        self.win.setCoords(-10, -10, 210, 155)
        Line(Point(-10, 0), Point(210, 0)).draw(self.win)
        for x in range(0, 210, 50):
            Text(Point(x, -7), str(x)).draw(self.win)
            Line(Point(x, 0), Point(x, 2)).draw(self.win)
        self.launcher = Launcher(self.win)
        self.shots = []

    def run(self):
        while True:
            self.update_shots(1/30)
            key = self.win.checkKey()
            if key in ["q", "Q"]:
                break
            if key == "Up":
                self.launcher.adj_angle(5)
            elif key == "Down":
                self.launcher.adj_angle(-5)
            elif key == "Right":
                self.launcher.adj_angle(5)
            elif key == "Left":
                self.launcher.adj_angle(-5)
            elif key in ["f", "F"]:
                self.shots.append(self.launcher.fire())  

            update(30)
        self.win.close()

    def update_shots(self, dt):
        alive = []
        for shot in self.shots:
            shot.update(dt)

            if shot.get_y() >= 0 or shot.get_x() >= -10 or shot.get_x() <= 210:
                alive.append(shot)
            else:
                shot.undraw()
        self.shots = alive

ProjectileApp().run()