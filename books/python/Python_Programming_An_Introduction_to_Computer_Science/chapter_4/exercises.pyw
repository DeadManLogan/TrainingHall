from graphics import *
import random
import math

# EXERCISE 1
def exercise_1():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(100,100))
    shape.setOutline('red')
    shape.setFill('red')
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        cloned_shape = shape.clone()
        cloned_shape.draw(win)
        c = cloned_shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        cloned_shape.move(dx, dy)
    
    message = Text(Point(100,100), 'Click again to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

# EXERCISE 2
def exercise_2():
    win = GraphWin('Exercise 2', 1000, 1000)

    first_circle = Circle(Point(500,500), 150)
    first_circle.setFill('white')
    first_circle.draw(win)

    circle_colors = ['black', 'blue', 'red', 'yellow']

    for i,color in enumerate(circle_colors):
        i += 1
        new_circle = Circle(first_circle.getCenter(), first_circle.getRadius() - (i*30))
        new_circle.setFill(color)
        new_circle.draw(win)

    win.getMouse()
    win.close()

# EXERCISE 3
def exerceise_3():
    win = GraphWin('Exercise 3', 500, 500)

    face = Circle(Point(250,250), 200)
    face.setFill('salmon')
    face.draw(win)

    left_eye = Oval(Point(175,200), Point(200,90))
    left_eye.setFill('black')
    left_eye.draw(win)

    right_eye = Oval(Point(300,200), Point(325,90))
    right_eye.setFill('black')
    right_eye.draw(win)

    win.getMouse()
    win.close()

# EXERCISE 5
def draw_die(value):
    background = Rectangle(Point(20, 20), Point(180, 180)) 

    if value == 1:
        number_1 = Circle(Point(100, 100), 10)
        return background, number_1
    elif value == 2:
        number_1 = Circle(Point(50, 50), 10)
        number_2 = Circle(Point(150, 150), 10)
        return background, number_1, number_2
    elif value == 3:
        number_1 = Circle(Point(100, 100), 10)
        number_2 = Circle(Point(50, 150), 10)
        number_3 = Circle(Point(150, 50), 10)
        return background, number_1, number_2, number_3
    elif value == 4:
        number_1 = Circle(Point(50, 50), 10)
        number_2 = Circle(Point(50, 150), 10)
        number_3 = Circle(Point(150, 50), 10)
        number_4 = Circle(Point(150, 150), 10)
        return background, number_1, number_2, number_3, number_4
    elif value == 5:
        number_1 = Circle(Point(50, 50), 10)
        number_2 = Circle(Point(50, 150), 10)
        number_3 = Circle(Point(150, 50), 10)
        number_4 = Circle(Point(150, 150), 10)
        number_5 = Circle(Point(100, 100), 10)
        return background, number_1, number_2, number_3, number_4, number_5
    else:
        number_1 = Circle(Point(50, 50), 10)
        number_2 = Circle(Point(50, 150), 10)
        number_3 = Circle(Point(150, 50), 10)
        number_4 = Circle(Point(150, 150), 10)
        number_5 = Circle(Point(50, 100), 10)
        number_6 = Circle(Point(150, 100), 10)
        return background, number_1, number_2, number_3, number_4, number_5, number_6


def exercise_5():
    win = GraphWin('Exercise 5', 200,200)

    for i in range(15):
        number = random.randint(1, 6)
        elements = draw_die(number)
        [element.draw(win) for element in elements]
        win.getMouse()
        [element.undraw() for element in elements]

    win.getMouse()
    win.close()

# EXERCISE 6
def exercise_6():
    win = GraphWin ("Exercise_6", 800, 800)

    principal_message = Text(Point(80, 40), 'Initial principal:')
    principal_message.draw(win)
    principal = Entry(Point(160, 40), 3)
    principal.draw(win)

    apr_message = Text(Point(80, 70), 'Interest rate:')
    apr_message.draw(win)
    apr = Entry(Point(160, 70), 3)
    apr.draw(win)

    win.getMouse()

    principal = float(principal.getText())
    apr = float(apr.getText())

    win.setBackground ("white")
    win.setCoords(-1.75 , -200 , 11.5 , 10400)
    Text(Point(-1, 0), 'O.OK').draw(win)
    Text(Point(-1, 2500), '2.5K').draw(win)
    Text(Point(-1, 5000), '5.0K').draw(win)
    Text(Point(-1, 7500), '7.5k').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill ("green")
    bar.setWidth (2)
    bar.draw (win)

    for year in range(1, 11):
        principal = principal*(1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    win.getMouse()
    win.close()

# EXERCISE 7
def exercise_7():
    win = GraphWin ("Exercise_7", 500, 500)
    win.setCoords(-10, -10, 10, 10)

    rad = float(input('Radius: '))
    y_intercept = int(input('Y-interception: '))

    circle = Circle(Point(0, 0), rad)
    circle.draw(win)

    line = Line(Point(-10, y_intercept), Point(10, y_intercept))
    line.draw(win)

    red_x1 = round(abs(math.sqrt(rad**2 - y_intercept**2)), 1)
    red_x2 = -red_x1

    red_point1 = Point(red_x1, y_intercept)
    red_point1.setOutline('red')
    red_point1.draw(win)

    red_point2 = Point(red_x2, y_intercept)
    red_point2.setOutline('red')
    red_point2.draw(win)

    result = Text(Point(0, 5), f'Point 1: {red_point1} Point 2: {red_point2}')
    result.draw(win)

    win.getMouse()
    win.close()

# EXERCISE 8
def exercise_8():
    win = GraphWin ("Exercise_8", 500, 500)
    win.setCoords(-10, -10, 10, 10)

    start_point = win.getMouse()
    end_point = win.getMouse()

    line = Line(start_point, end_point)
    line.setOutline('cyan')
    line.draw(win)

    dx = end_point.getX() - start_point.getX()
    dy = end_point.getY() - start_point.getY()
    slope = round(dy/dx, 1)
    length = round(math.sqrt(dx**2 + dy**2), 1)

    result = Text(Point(2, 2), f'Length: {length} Slope: {slope}')
    result.draw(win)

    win.getMouse()
    win.close()

# EXERCISE 9
def exercise_9():
    win = GraphWin ("Exercise_9", 500, 500)
    win.setCoords(-10, -10, 10, 10)

    start_point = win.getMouse()
    end_point = win.getMouse()

    rect = Rectangle(start_point, end_point)
    rect.draw(win)

    width = abs(start_point.getX() - end_point.getX())
    length = abs(start_point.getY() - end_point.getY())
    area = length*width
    perimeter = 2*(length + width)
    
    result = Text(Point(2, 2), f'Area: {area} Perimeter: {perimeter}')
    result.draw(win)

    win.getMouse()
    win.close()

# EXERCISE 10
def line_length(start_point_x, start_point_y, end_point_x, end_point_y):
    dx = end_point_x - start_point_x
    dy = end_point_y - start_point_y
    length = round(math.sqrt(dx**2 + dy**2), 1)

    return length


def exercise_10():
    win = GraphWin ("Exercise_10", 500, 500)
    win.setCoords(-10, -10, 10, 10)

    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()

    line_1_2 = Line(point1, point2)
    line_1_2.draw(win)
    line_1_3 = Line(point1, point3)
    line_1_3.draw(win)
    line_2_3 = Line(point2, point3)
    line_2_3.draw(win)

    length1 = line_length(point1.getX(), point1.getY(), point2.getX(), point2.getY())
    length2 = line_length(point1.getX(), point1.getY(), point3.getX(), point3.getY())
    length3 = line_length(point2.getX(), point2.getY(), point3.getX(), point3.getY())

    s = (length1 + length2 + length3) / 2
    area = round(math.sqrt(s*(s - length1)*(s - length2)*(s - length3)), 1)
    perimeter = round(length1 + length2 + length3, 1)
    
    result = Text(Point(2, 2), f'Area: {area} Perimeter: {perimeter}')
    result.draw(win)

    win.getMouse()
    win.close()

# EXERCISE 11
def exercise_11():
    win = GraphWin ("Exercise_10", 500, 500)
    win.setCoords(-10, -10, 10, 10)

    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    point4 = win.getMouse()
    point5 = win.getMouse()

    rect = Rectangle(point1, point2)
    rect.draw(win)

    house_frame = abs(point1.getX() - point2.getX())

    line = Line(Point(point3.getX()-(house_frame*0.1), point3.getY()), Point(point3.getX()+(house_frame*0.1), point3.getY()))
    line.draw(win)
    side1 = Line(Point(point3.getX()-(house_frame*0.1), point3.getY()), Point(point3.getX()-(house_frame*0.1), point1.getY()))
    side1.draw(win)
    side2 = Line(Point(point3.getX()+(house_frame*0.1), point3.getY()), Point(point3.getX()+(house_frame*0.1), point1.getY()))
    side2.draw(win)

    leftWindow_X = point4.getX() - (0.05 * house_frame)
    leftWindow_Y = point4.getY() - (0.05 * house_frame)
    rightWindow_X = point4.getX() + (0.05 * house_frame)
    rightWindow_Y = point4.getY() + (0.05 * house_frame)
    window = Rectangle(Point(leftWindow_X, leftWindow_Y), Point(rightWindow_X, rightWindow_Y))
    window.draw(win)

    line_1 = Line(point5, point2)
    line_1.draw(win)
    line_2 = Line(point5, Point(point1.getX(), point2.getY()))
    line_2.draw(win)


    win.getMouse()
    win.close()

exercise_11()