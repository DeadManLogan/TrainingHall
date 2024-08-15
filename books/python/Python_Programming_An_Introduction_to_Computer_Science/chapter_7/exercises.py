def temperature():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = 9/5 * celsius + 32
    print(f"Fahrenheit: {fahrenheit}")

    if fahrenheit > 90:
        print("HEAT")
    if fahrenheit < 30:
        print("COLD")