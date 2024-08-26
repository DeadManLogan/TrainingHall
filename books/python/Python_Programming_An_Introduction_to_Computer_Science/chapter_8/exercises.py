import math

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

exercise_5()