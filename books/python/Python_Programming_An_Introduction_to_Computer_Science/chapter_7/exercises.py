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
        



exercise_6()