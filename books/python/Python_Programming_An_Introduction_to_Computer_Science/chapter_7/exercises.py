from graphics import *
import math

# EXERCISE 1
def exercise_1():
    hours = float(input("Enter the hours you worked: "))
    rate = float(input("Enter the hourly rate: "))

    try:
        if hours <= 40:
            week_wage = hours * rate
            print(f"Your weekly wage is: {week_wage}")
        else:
            week_wage = 40 * rate + (hours - 40) * rate * 1.5
            print(f"Your weekly wage is: {week_wage}")
    except ValueError as error:
        print(error)

# EXERCSE 2
def exercise_2():
    score = input("Enter the quizz score (1-5): ")

    if score == "5":
        print("A")
    elif score == "4":
        print("B")
    elif score == "3":
        print("C")
    elif score == "2":
        print("D")
    elif score == "1":
        print("E")
    else:
        print("Inalid score.")

# EXERCISE 3
def exercise_3():
    score = int(input("Enter the quizz score (0-100): "))

    if score <= 100 and score >= 90:
        print("A")
    elif score <= 89 and score >= 80:
        print("B")
    elif score <= 79 and score >= 70:
        print("C")
    elif score <= 69 and score >= 60:
        print("D")
    elif score < 60 and score >= 0:
        print("E")
    else:
        print("Invalid score.")

# EXERCISE 4
def exercise_4():
    credits = int(input("Enter your total credits: "))

    if credits >= 0 and credits < 7:
        print("You are a Freshman.")
    if credits >= 7 and credits < 16:
        print("You are a Sophomore.")
    if credits >= 16 and credits < 26:
        print("You are a Junior.")
    if credits >= 26:
        print("You are a Senior.")
    else:
        print("Invalid credits.")

# EXERCISE 5
def calculate_bmi(weight, height):
    bmi = (weight * 720) / height ** 2
    return bmi

def exercise_5():
    try:
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))
        bmi = calculate_bmi(weight, height)
    except ValueError:
        print("Weight and height must be numbers.")


    if bmi >= 19 and bmi <= 25:
        print("You are within the healthy range.")
    elif bmi < 19:
        print("You are below the healthy range.")
    else:
        print("You are above the healthy range.")

# EXERCISE 6
def exercise_6():
    try:
        speed_limit = int(input("Enter the speed limit of the road: "))
        clocked_speed = int(input("Enter the vehicle's speed: "))
    except:
        print("Inputs must be integers.")

    speed_difference = clocked_speed - speed_limit

    if clocked_speed > speed_limit:
        fine = 50
        if clocked_speed > 90:
            fine += 200
        if (speed_difference) > 0:
            fine += speed_difference * 5
        print(f"You have to pay {fine}$.")
    else:
        print("Legal speed.")
        
# EXERCISE 7
def calculate_price(s_hours, e_hours, s_minutes, e_minutes):
    price = 0

    if (e_hours - 21) >= 0:
        total_h = 21 - s_hours
        price = total_h * 2.5

        price += (e_hours - 21) * 1.75

        if (s_minutes - e_minutes) <= 0:
            price += 1.75
    else:
        total_h = e_hours - s_hours
        price = total_h * 2.5

        if (s_minutes - e_minutes) <= 0:
            price += 2.5

    return price

def exercise_7():
    starting_time = input("Enter the starting time in hours and minutes (e.g. 12:34): ")
    s_hours, s_minutes = starting_time.split(":")
    s_hours, s_minutes = int(s_hours), int(s_minutes)

    ending_time = input("Enter the ending time in hours and minutes (e.g. 18:34): ")
    e_hours, e_minutes = ending_time.split(":")
    e_hours, e_minutes = int(e_hours), int(e_minutes)

    price = calculate_price(s_hours, e_hours, s_minutes, e_minutes)
    print(price)

# EXERCISE 8
def exercise_8():
    age = int(input("Enter your age: "))
    years_cit = int(input("Enter for how long you are a US citizen: "))

    if (age >= 30) and (years_cit >= 9):
        print("You can become a Senator or a House representative!")
    elif (age >= 25) or (age < 30) and (years_cit >= 7) or (years_cit < 9):
        print("You can become House representative.")
    else:
        print("You are a peasant.")

# EXERCISE 9
def easter(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = ((19 * a) + 24) % 30
    e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7

    date = 22 + d + e
    if date > 31:
        print(f"Easter is on April, {date - 31}")
    else:
        print(f"Easter is on March, {date}")

def exercise_9():
    year = int(input("Enter a year between 1982 - 2048: "))
    if year < 1982 or year > 2048:
        year = int(input("The input was not correct. Enter a year between 1982 - 2048: "))
    
    easter(year)

# EXERCISE 10def easter(year):
def easter_mod(year):
    special_years = [1954, 1981, 2049, 2076]
    a = year % 19
    b = year % 4
    c = year % 7
    d = ((19 * a) + 24) % 30
    e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7

    date = 22 + d + e
    if year in special_years:
        date -= 7
    if date > 31:
        print(f"Easter is on April, {date - 31}")
    else:
        print(f"Easter is on March, {date}")

def exercise_10():
    year = int(input("Enter a year between 1900 - 2099: "))
    if year < 1900 or year > 2099:
        year = int(input("The input was not correct. Enter a year between 1900 - 2099: "))
    
    easter_mod(year)

# EXERCISE 11
def leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leap year.")
        else:
            print(f"{year} is not leap year.")
    elif year % 4 == 0:
        print(f"{year} is leap year.")
    else:
        print(f"{year} is not a leap year.")

def exercise_11():
    year = int(input("Enter a year: "))
    leap_year(year)

# EXERCISE 12
def valid_date(year):
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]

    month = int(year[0])
    day = int(year[1])
    year = int(year[2])

    if year % 100 == 0:
        if year % 400 == 0:
            leap = 1
        else:
            leap = 0
    elif year % 4 == 0:
        leap = 1
    else:
        leap = 0

    if month < 0 or month > 12:
        print("Not a real date")
    
    if (day > 31 or day < 1) and month not in months_31:
        print("Not a real date")
    elif (day > 30 or day < 1) and month not in months_30:
        print("Not a real date")
    elif leap == 1 and (day > 29 or day < 1):
        print("Not a real date")
    elif leap == 0 and (day > 28 or day < 1):
        print("Not a real date")
    else:
        print("It's a real date.")

def exercise_12():
    date = input("Enter a date in the format MM/dd/YYYY: ").split("/")
    valid_date(date)

# EXERCISE 13
def calculate_day_num(month, day, year):
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]

    day_num = 31 * (month - 1) + day

    if year % 100 == 0:
        if (year % 400 == 0) and ((month == 2 and day > 29) or (month > 2)):
            day_num -= ((4 * month) + 23) // 10
            day_num += 1
        elif month > 2:
            day_num -= ((4 * month) + 23) // 10
    elif (year % 4 == 0) and ((month == 2 and day > 29) or (month > 2)):
        day_num -= ((4 * month) + 23) // 10
        day_num += 1
    elif month > 2:
        day_num -= ((4 * month) + 23) // 10
    
    return day_num

def exercise_13():
    date = input("Enter a date in the format MM/dd/YYYY: ").split("/")
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
    num = calculate_day_num(month, day, year)
    print(f"The number of the day is: {num}")

# EXERCISE 14
def draw_points(win, rad, y_intercept):
    if rad == y_intercept:
        red_x1 = round(abs(math.sqrt(rad**2 - y_intercept**2)), 1)
        red_x2 = -red_x1

        red_point1 = Point(red_x1, y_intercept)
        red_point1.setOutline('red')
        red_point1.draw(win)

        result = Text(Point(0, 5), f'Point 1: {red_point1}')
        result.draw(win)
    else:
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

def exercise_14():
    win = GraphWin ("Exercise_14", 500, 500)
    win.setCoords(-10, -10, 10, 10)

    rad = float(input('Radius: '))
    y_intercept = int(input('Y-interception: '))

    circle = Circle(Point(0, 0), rad)
    circle.draw(win)

    line = Line(Point(-10, y_intercept), Point(10, y_intercept))
    line.draw(win)

    draw_points(win, rad, y_intercept)

    win.getMouse()
    win.close()

# EXERCISE 15
def exercise_15():
    win = GraphWin ("Exercise_15", 500, 500)
    win.setCoords(-10, -10, 10, 10)

    start_point = win.getMouse()
    end_point = win.getMouse()

    line = Line(start_point, end_point)
    line.setOutline('cyan')
    line.draw(win)

    dx = end_point.getX() - start_point.getX()
    dy = end_point.getY() - start_point.getY()

    if dx == 0:
        print("Line should not be vertical.")
    else:
        slope = round(dy/dx, 1)
        length = round(math.sqrt(dx**2 + dy**2), 1)

        result = Text(Point(2, 2), f'Length: {length} Slope: {slope}')
        result.draw(win)

    win.getMouse()
    win.close()

# EXERCISE 16
def count_score(distance_from_center):
    if distance_from_center <= 30:
        arrow_score = 9
    elif distance_from_center <= 60:
        arrow_score = 7
    elif distance_from_center <= 90:
        arrow_score = 5
    elif distance_from_center <= 120:
        arrow_score = 3
    elif distance_from_center <= 150:
        arrow_score = 1
    else:
        arrow_score = 0
    return arrow_score

def draw_target(win):
    first_circle = Circle(Point(350,350), 150)
    first_circle.setFill('white')
    first_circle.draw(win)

    circle_colors = ['black', 'blue', 'red', 'yellow']
    score = 0

    for i,color in enumerate(circle_colors):
        i += 1
        new_circle = Circle(first_circle.getCenter(), first_circle.getRadius() - (i*30))
        new_circle.setFill(color)
        new_circle.draw(win)
    
    for j in range(5):
        x = j+1
        spot = win.getMouse()
        distance_from_center = math.sqrt((spot.getX() - 350) ** 2 + (spot.getY() - 350) ** 2)
        
        arrow_score = count_score(distance_from_center)

        score += arrow_score
        score_text = Text(Point(50, 40), "Score:")
        score_text.draw(win)
        score_message = Text(Point(x*80, 40), arrow_score)
        score_message.draw(win)

    win.getMouse()
    total_score = Text(Point(80, 60), f"Total score: {score}")
    total_score.draw(win)
    
def exercise_16():
    win = GraphWin('Exercise 16', 700, 700)

    draw_target(win)

    win.getMouse()
    win.close()

# EXERCISE 17
def exercise_17():
    win = GraphWin('Exercise 17', 400, 400)

    radius = 10
    circle = Circle(Point(200,200), radius)
    circle.setFill('white')
    circle.draw(win)

    dx, dy = 1, 1

    for _ in range(1000):
        circle.move(dx, dy)
        center = circle.getCenter()
        x = center.getX()
        y = center.getY()

        if x + radius >= 400 or x - radius <= 0:
            dx = -dx
        if y + radius >= 400 or y - radius <= 0:
            dy = -dy
        update(30)

    win.getMouse()
    win.close()

# EXERCISE 18
def exercise_18():
    win = GraphWin ("Exercise_18", 500, 500)
    win.setCoords(-10, -10, 10, 10)

    point1 = win.getMouse()
    point2 = win.getMouse()

    point3 = win.getMouse()
    if point3.getX() <= point1.getX() or point3.getX() >= point2.getX():
        print("The door needs to be between doors.")
        point3 = win.getMouse()
    if point3.getY() <= point1.getY() or point3.getY() >= point2.getY():
        print("The door needs to be between floor and ceiling.")
        point3 = win.getMouse()

    point4 = win.getMouse()
    if point4.getX() <= point1.getX() or point4.getX() >= point2.getX():
        print("The door needs to be between doors.")
        point4 = win.getMouse()
    if point4.getY() <= point1.getY() or point4.getY() >= point2.getY():
        print("The door needs to be between floor and ceiling.")
        point4 = win.getMouse()

    point5 = win.getMouse()
    if point5.getY() <= point2.getY():
        print("Buddy we need a roof.")
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

exercise_18()