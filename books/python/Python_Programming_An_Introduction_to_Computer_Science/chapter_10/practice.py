import math

class Projectile:
    def __init__(self, angle, velocity, height):
        self.x_pos = 0.0
        self.y_pos = height
        theta = math.radians(angle)
        self.x_vel = velocity * math.cos(theta)
        self.y_vel = velocity * math.sin(theta)

    def get_x(self):
        return self.x_pos
    
    def get_y(self):
        return self.y_pos
    
    def update(self, time):
        self.x_pos += time * self.x_vel
        y_vel1 = self.y_vel - time * 9.8
        self.y_pos += time * (self.y_vel + y_vel1) / 2.0
        self.y_vel = y_vel1

def cannonball():
    angle = float(input("Enter the angle of the cannon: "))
    vel = float(input("Enter the initial velocity: "))
    time = float(input("Enter the time interval between calculations: "))
    h0 = float(input("Enter the initial height: "))

    c_ball = Projectile(angle, vel, h0)
    while c_ball.get_y() >= 0:
        c_ball.update(time)
    print(c_ball.get_x())

cannonball()

