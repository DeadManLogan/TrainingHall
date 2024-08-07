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

# def exercise_4():


exercise_3()