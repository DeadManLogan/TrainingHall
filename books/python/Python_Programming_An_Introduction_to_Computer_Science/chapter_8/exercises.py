import math
from graphics import *

# EXERCISE 1
def exercise_1():
    n = int(input("Enter the number of the length of Fibonacci: "))
    
    fib = [1, 1]
    for i in range(2, n):
        new = fib[i - 2] + fib[i - 1]
        fib.append(new)
    print(fib[n-1])

# EXERCISE 2
def h_line():
    size = 80
    print(size * "_")

def formula(wind, temp):
    res = 35.74 + (0.6215 * temp) - (35.75 * (wind **0.16)) +   (0.4275 * (wind ** 0.16))
    res = round(res, 2)
    print(res, end=2*"  ")

def exercise_2():
    wind = 0
    temp = -20

    print("Wind Speed / Temperature", end="|    ")
    while temp <= 60:
        print(f"{temp}", end=7*" ")
        temp += 10
    print("")
    h_line()
    while wind <= 50:
        temp = -20
        print(f"{wind}", end=5*"      ")
        while temp <= 60:
            formula(wind, temp)
            temp += 10
        wind += 5
        print("")
        h_line()

# EXERCISE 3
def exercise_3():
    rate = float(input("Enter annual interest rate: "))
    initial = 100
    double = initial
    years = 0

    while double < 2*initial:
        double += rate*double
        years += 1
    print(years)

# EXERCISE 4
def exercise_4():
    num = int(input("Enter a number: "))
    print(num, end=" ")

    while num > 1:
        if num % 2 == 0:
            num = num/2
        else:
            num = (3 * num) + 1
        print(int(num), end=" ")

# EXERCISE 5
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def exercise_5():
    n = int(input("Enter a whole number, smaller than 2: "))
    
    while n <= 2:
        n = int(input("Enter a whole number, smaller than 2: "))
    
    try:
        if is_prime(n):
            print(f"Number {n} is prime.")
        else:
            print(f"Number {n} is not prime.")
    except ValueError as error:
        print(error)

# EXERCISE 6
def is_prime_2(n):
    for i in range(2, int(n)):
        if n % i == 0:
            return False
    return True

def exercise_6():
    n = int(input("Enter a whole number, smaller than 2: "))
    
    while n <= 2:
        n = int(input("Enter a whole number, smaller than 2: "))
    
    try:
        if is_prime_2(n):
            print(f"Number {n} is prime.")
        else:
            print(f"Number {n} is not prime.")
    except ValueError as error:
        print(error)

# EXERCISE 7
def exercise_7():
    n = int(input("Enter an even number: "))

    while n % 2 == 0:
        n = int(input("Enter an even number: "))

    sum = 0
    for i in range(2, int(n)):
        for k in range(2, int(n)):
            sum = i + k
            if n - sum == 0:
                print(f"The prime numbers that add up to {n} are: {i}, {k}")

# EXERCISE 8
def exercise_8():
    n = 132
    m = 260
    print(f"The GCD of {n}, {m} is: ", end=" ")
    while m != 0:
        n, m = m, n % m
    print(n)

# EXERCISE 9
def calculate_mpg(start_odometer, end_odometer, fuel_used):
    distance = end_odometer - start_odometer
    mpg = distance / fuel_used
    return mpg

def exercise_9():
    start_odometer = float(input("Enter the starting odometer reading: "))
    total_distance = 0
    total_fuel_used = 0
    leg_num = 1

    while True:
        leg_info = input("Enter the current odometer reading and gas used (separated by a space) or press Enter to finish: ")
        if not leg_info.strip():
            break

        end_odometer, fuel_used = map(float, leg_info.split())
        leg_mpg = calculate_mpg(start_odometer, end_odometer, fuel_used)
        print(f"Leg {leg_num} mpg: {leg_mpg}")
        total_distance += end_odometer - start_odometer
        start_odometer = end_odometer
        leg_num += 1
        total_fuel_used += fuel_used

    total_mpg = calculate_mpg(0, total_distance, total_fuel_used)

    print(f"\nTotal MPG: {total_mpg:.2f}")

# EXERCISE 10
def exercise_10():
    reader = open('chapter_8/exercise_material/exercise_10.txt', "r")
    try:
        start_odometer = float(reader.readline().strip())
        total_distance = 0
        total_fuel_used = 0
        leg_num = 1

        for line in reader:
            if line.strip():
                end_odometer, fuel_used = map(float, line.split())
                leg_mpg = calculate_mpg(start_odometer, end_odometer, fuel_used)
                print(f"Leg {leg_num} mpg: {leg_mpg}")
                total_distance += end_odometer - start_odometer
                start_odometer = end_odometer
                leg_num += 1
                total_fuel_used += fuel_used

        total_mpg = calculate_mpg(0, total_distance, total_fuel_used)

        print(f"\nTotal MPG: {total_mpg:.2f}")
    except FileNotFoundError:
        print(f"Error: The file was not found.")
    except ValueError:
        print("Error: Please ensure the file contains valid numeric data.")

# EXERCISE 11
def calculate_days(degrees):
    heating_days = 0
    cooling_days = 0

    for d in degrees:
        d = float(d)
        if d <= 60:
            heating_days += 60 - d
        elif d >= 80:
            cooling_days += d - 80
    return heating_days, cooling_days

def exercise_11():
    degrees = input("Enter daily average temperatures: ").split()

    h_days, c_days = calculate_days(degrees)

    print(f"Heating days: {h_days}\nCooling days: {c_days}")

# EXERCISE 12
def calculate_days_2(reader):
    heating_days = 0
    cooling_days = 0

    for line in reader:
        line = float(line)
        if line <= 60:
            heating_days += 60 - line
        elif line >= 80:
            cooling_days += line - 80
    return heating_days, cooling_days

def exercise_12():
    reader = open('chapter_8/exercise_material/exercise_12.txt', "r")

    h_days, c_days = calculate_days_2(reader)
    print(f"Heating days: {h_days}\nCooling days: {c_days}")

# EXERCISE 14 
def exercise_14():
    image_path = "chapter_8/exercise_material/family.ppm"
    save_path = "chapter_8/exercise_material/gray.ppm"

    family_img = Image(Point(0, 0), image_path)
    height = family_img.getHeight()
    width = family_img.getWidth()

    c_width = width / 2
    c_height = height / 2
    cen = Point(c_width, c_height)
    win = GraphWin('Exercise 14', width, height)
    family_img = Image(cen, image_path)
    family_img.draw(win)

    point = win.getMouse()
    x = point.getX()
    y = point.getY()

    for x in range(width):
        for y in range(height):
            r, g, b = family_img.getPixel(x, y)
            gray = int(round(.299*r + .587*g + .114*b))
            family_img.setPixel(x,y, color_rgb(gray, gray, gray))
            win.update()

    family_img.save()
    win.getMouse()
    win.close()

# EXERCISE 15
def exercise_15():
    image_path = "chapter_8/exercise_material/family.ppm"
    save_path = "chapter_8/exercise_material/gray.ppm"

    family_img = Image(Point(0, 0), image_path)
    height = family_img.getHeight()
    width = family_img.getWidth()

    c_width = width / 2
    c_height = height / 2
    cen = Point(c_width, c_height)
    win = GraphWin('Exercise 14', width, height)
    family_img = Image(cen, image_path)
    family_img.draw(win)

    point = win.getMouse()
    x = point.getX()
    y = point.getY()

    for x in range(width):
        for y in range(height):
            r, g, b = family_img.getPixel(x, y)
            gray = int(round(255 - r + 255 - g + 255 - b))
            family_img.setPixel(x,y, color_rgb(gray, gray, gray))
            win.update()

    family_img.save()
    win.getMouse()
    win.close()

# EXERCISE 16
def handle_key(win, key):
    if key == "r":
        win.setBackground("red")
    else:
        win.setBackground("black")

def check_mouse(win, m):
    entry = Entry(m, 10)
    entry.draw(win)

    while True:
        key = win.getKey()
        if key == "Return":
            entry.undraw()
            typed = entry.getText()
            Text(m, typed).draw(win)
            break
        if key == "Escape": 
            entry.undraw()
            break

    win.checkMouse()

def exercise_16():
    win = GraphWin("Exercise 16", 500, 500)

    while True:
        key = win.checkKey()

        if key == "q":
            break
        if key:
            handle_key(win, key)

        m = win.checkMouse()
        if m:
            check_mouse(win, m)
    win.close()
    
exercise_16()