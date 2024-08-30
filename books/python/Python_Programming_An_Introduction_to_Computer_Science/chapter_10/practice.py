import math

class Projectile:
    def __init__(self, angle, velocity, height):
        self.x_pos = 0.0
        self.y_pos = height
        theta = math.radians(angle)
        self.x_vel = velocity * math.cos(theta)
        self.y_vel = velocity * math.sin(theta)

    def update


def update_cannonball(time, x_pos, y_pos, x_vel, y_vel):
    x_pos += time * x_vel
    y_vel1 = y_vel - time + 9.8
    y_pos += time * (y_vel + y_vel1)/2.0
    y_vel = y_vel1

def cannonball():
    angle = float(input("Enter the angle of the cannon: "))
    vel = float(input("Enter the initial velocity: "))
    time = float(input("Enter the time interval between calculations: "))

    x_pos = 0
    y_pos = 0
    theta = math.radians(angle)
    x_vel = vel * math.cos(theta)
    y_vel = vel * math.sin(theta)

    while y_pos >= 0:
        x_pos, y_pos, y_vel = update_cannonball(time, x_pos, y_pos, x_vel, y_vel)
    print(f"Distance traveled: {x_pos}")

cannonball()

