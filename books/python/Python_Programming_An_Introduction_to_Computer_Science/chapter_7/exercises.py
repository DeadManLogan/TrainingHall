import math

def temperature():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = 9/5 * celsius + 32
    print(f"Fahrenheit: {fahrenheit}")

    if fahrenheit > 90:
        print("HEAT")
    if fahrenheit < 30:
        print("COLD")

def main():
    print("This program finds the real solutions to a quadrantic\n")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discrim = b*b - 4*a*c
    if discrim > 0:
        disc_root = math.sqrt(discrim)
        root_1 = (-b + disc_root)/(2*a)
        root_2 = (-b - disc_root)/(2*a)
        print(f"Solutions: {root_1}, {root_2}")
    elif discrim == 0:
        root = -b/(2*a)
        print(f"Double root: {root}")
    else:
        print("No real roots.")

if __name__ == "__main__":
    main()