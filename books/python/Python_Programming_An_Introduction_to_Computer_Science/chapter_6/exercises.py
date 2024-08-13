import math

# EXERCISE 1
def lyrics_1(animals, sounds):
    for i in range(len(animals)):
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
        print(f"And on that farm he had a {animals[i]}, Ee-igh, Ee-igh, Oh!")
        print(f"With a {sounds[i]}, {sounds[i]} here and a {sounds[i]}, {sounds[i]} there.")
        print(f"Here a {sounds[i]}, there a {sounds[i]}, everywhere a {sounds[i]}, {sounds[i]}.")
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n")

def exercise_1():
    animals = ['cow', 'dog', 'cat', 'frog', 'bee']
    sounds = ['moo', 'woof', 'meow', 'croak', 'buzzes']
    lyrics_1(animals, sounds)

# EXERCISE 2
def lyrics_2(activities):
    for i in range(len(activities)):
        print(f"""The ants go marching {i+1} by {i+1}, hurrah, hurrah
The ants go marching {i+1} by {i+1}, hurrah, hurrah
The ants go marching {i+1} by {i+1},
The little one stops to {activities[i]}
And they all go marching down to the ground
To get out of the rain, BOOM! BOOM! BOOM!
""")

def exercise_2():
    activities = ["suck his thumb", "tie his shoe", "climb a tree", "shut the door", "take a dive", 
                  "pick up sticks", "pray to heaven", "roller skate", "check the time", "shout 'The End'"]
    lyrics_2(activities)

# EXERCISE 3
def sphere_area(radius):
    area = 4 * math.pi * radius**2
    return area

def sphere_volume(radius):
    volume = 4/3 * math.pi * radius**3
    return volume

def exercise_3():
    radius = float(input("Enter the radius of the sphere: "))
    area = sphere_area(radius)
    volume = sphere_volume(radius)
    print(f"Area: {area}\nVolume: {volume}")

# EXERCISE 4
def sum_n(n):
    sum = (n*(n+1))/2
    return sum
def sum_n_cubes(n):
    cube_sum = (n**2*((n+1)**2))/4
    return cube_sum

def exercise_4():
    n = int(input("Enter a natural number: "))
    sum, cube_sum = sum_n(n), sum_n_cubes(n)
    print(f"Sum: {sum}\nCube Sum: {cube_sum}")

# EXERCISE 5
def pizza_area(diameter):
    area = math.pi * ((diameter/2)**2)
    return area

def cost_per_inch(price, area):
    cost = price/area
    return cost

def exercise_5():
    diameter = float(input("Enter the diameter of the pizza: "))
    price = float(input("Enter the price of the pizza: "))
    area = pizza_area(diameter)
    cost = cost_per_inch(price, area)
    print(f"Cost per inch: {cost}")

# EXERCISE 6
def triangle_are(sides):
    semiperimeter = (sides[0] + sides[1] + sides[2])/2
    area = math.sqrt(semiperimeter * (semiperimeter - sides[0]) * (semiperimeter - sides[1]) * (semiperimeter - sides[2]))
    return area

def exercise_6():
    sides = input("Enter three triangle sides: ").split()
    sides = [float(i) for i in sides]
    area = triangle_are(sides)
    print(f"Triangle Area: {area}")

# EXERCISE 7
def fibonacci(n):
    num1 = 0
    num2 = 1
    next_num = num2
    count = 1

    while count <= n:
        print(next_num, end=" ")
        count += 1
        num1, num2 = num2, next_num
        next_num = num1 + num2

def exercise_7():
    n = int(input("Enter a positive natural number: "))
    print(fibonacci(n))

# EXERCISE 8
def next_guess(guess, x):
    next = (guess + x/guess)/2
    return next

def exercise_8():
    x = float(input("Enter a number: "))
    times = int(input("Enter the times to guess: "))
    guess = x/2
    for _ in range(times):
        final = next_guess(guess, x)
    print(abs(final - math.sqrt(x)))

# EXERCISE 9
def grade(score):
    scale = ['90:A', '80:B', '70:C', '60:D']

    for i in scale:
        if score >= int(i[:2]):
            return (i[3])
        elif score < 60:
            return ('F')

def exercise_9():
    score = int(input('Give the grade (0-100): '))
    print(grade(score))

# EXERCISE 10
def acronym(phrase):
    acronym = ""
    for word in phrase:
        acronym = acronym + word[0]
    return acronym

def exercise_10():
    phrase = input("Give a phrase: ").title().split()
    print(acronym(phrase))
    
# EXERCISE 11
def squareEach(nums):
    sq_nums = [i**2 for i in nums]
    return sq_nums

def exercise_11():
    nums = [1, 2, 3, 4, 5]
    sq_nums = squareEach(nums)
    print(sq_nums)

exercise_11()