import math

def temperature():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = 9/5 * celsius + 32
    print(f"Fahrenheit: {fahrenheit}")

    if fahrenheit > 90:
        print("HEAT")
    if fahrenheit < 30:
        print("COLD")

def quadrantic():
    print("This program finds the real solutions to a quadrantic\n")
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        disc_root = math.sqrt(b*b - 4*a*c)
        root_1 = (-b + disc_root)/(2*a)
        root_2 = (-b - disc_root)/(2*a)
        print(f"Solutions: {root_1}, {root_2}")
    except ValueError as error_obj:
        if str(error_obj) == "math domain error":
            print("No real roots.")
        else:
            print("Invalid coefficient given.")
    except:
        print("Something went wrong.")

def main():
    x1, x2, x3 = eval(input("Enter three numbers: "))

    if (x1 > x2) and (x1 > x3):
        print(f"Max number is: {x1}")
    elif (x2 > x1) and (x2 > x3):
        print(f"Max number is: {x2}")
    else:
        print(f"Max number is: {x3}")

if __name__ == "__main__":
    main()