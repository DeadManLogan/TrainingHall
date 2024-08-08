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

exercise_8()