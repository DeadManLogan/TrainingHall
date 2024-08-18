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

exercise_1()