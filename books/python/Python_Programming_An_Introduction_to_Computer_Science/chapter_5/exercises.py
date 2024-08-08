def exercise_2():
    scale = ['5-A', '4-B', '3-C', '2-D', '1-F', '0-F']
    grade = int(input('Give the grade (0-5): '))

    for i in scale:
        if grade == int(i[0]):
            print(i[2])

def exercise_3():
    scale = ['90:A', '80:B', '70:C', '60:D']
    grade = int(input('Give the grade (0-100): '))

    for i in scale:
        if grade >= int(i[:2]):
            print(i[3])
            break
        elif grade < 60:
            print('F')
            break

def exercise_4():
    phrase = input("Give a phrase: ").title().split()
    acronym = ""
    for word in phrase:
        acronym = acronym + word[0]
    print(acronym)

def exercise_5():
    name = input("Enter a name: ").lower()
    number = 0
    for ch in name:
        number += ord(ch) - 96
    print(number)

def exercise_6():
    name = input("Enter a name: ").lower().replace(" ", "")
    number = 0
    for ch in name:
        number += ord(ch) - 96
    print(number)

def exercise_7():
    string = input("Enter the string to be encoded: ")
    key = int(input("Enter the key: "))

    msg = ""
    for i in string:
        msg = msg +  chr(ord(i) + key)
    print(msg)

def exercise_8():
    string = input("Enter the string to be encoded: ").lower()
    key = int(input("Enter the key: "))

    msg = ""
    for ch in string:
        n = ord(ch)
        if ord('a') <= n <= ord('z'):
            n -= ord('a')
            n = (n + key) % 26
            n += ord('a')
            msg = msg + chr(n)
        else:
            msg = msg + ch
    print(msg)

def exercise_9():
    sen = input("Enter words: ").split()
    print(f"There are {len(sen)} words in your sentence.")

def exercise_10():
    sen = input("Enter words: ").split()

    sum = 0
    for w in sen:
        sum += len(w) 
    print(f"Average word lenght: {sum/len(sen)}")

def exercise_11():
    num1, num2 = input("Enter 2 numbers: ").split()
    num1 = float(num1)
    num2 = float(num2)
    iterations = int(input("Enter the number of iterations: "))

    print(f"index    {num1}      {num2}\n----------------------------------")
    for i in range(iterations):
        num1 = 3.9 * num1 * (1 - num1)
        num2 = 3.9 * num2 * (1 - num2)
        print(f"{iterations}    {num1}      {num2}")

def exercise_12():
    principal = float(input("Enter the starting investment: "))
    apr = float(input("Enter the interst rate: "))
    years = int(input("Enter the years to invest: "))

    print("Year     Value\n--------------------")
    for i in range(years):
        principal += apr*principal
        print(f"{i}     ${principal}")

def exercise_13_12():
    reader = open('chapter_5/exercise_material/input.txt', 'r')
    writer = open('chapter_5/exercise_material/output.txt', 'w')
    inputs = []

    for line in reader:
        inputs.append(float(line))

    print("Year     Value\n--------------------", file=writer)
    for i in range(int(inputs[2])):
        inputs[0] += inputs[1]*inputs[0]
        print(f"{i+1}     ${inputs[0]}", file=writer)
    reader.close(), writer.close()

def exercise_14():
    file = input("Enter the path of the input file: ")
    reader = open(file, 'r')

    lines = 0
    words = 0
    characters = 0
    for line in reader:
        lines += 1
        words_per_line = line.split()
        words += len(words_per_line)
        for ch in words_per_line:
            characters += len(ch)

    print(f"Lines: {lines}  Words: {words}  Characters: {characters}")



exercise_14()