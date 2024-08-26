from graphics import *

def pract():
    n = input("Enter a number (empty to quit): ")
    total = 0
    count = 0
    while n != "":
        n = float(n)
        total += n
        count += 1
        n = input("Enter a number (negative to quit): ")
    avg = total / count
    print(f"Average: {avg}")

def file_avg():
    file_path = "chapter_8/practice_mat/input.txt"
    reader = open(file_path, "r")

    total = 0
    count = 0
    line = reader.readline()
    while line != "":
        for digit in line.split(","):
            try:
                total += float(digit)
                count += 1
            except ValueError as e:
                print(e)
        line = reader.readline()
    print(f"Average: {total/count}")

def score():
    a, b = 0, 0
    while (a < 15 or b < 15) and (abs(a - b) >= 2):
        a += 1
        b += 2
    print()

def handle_key(win, key):
    if key == "r":
        win.setBackground("red")
    else:
        win.setBackground("black")

def check_mouse(win, m):
    entry = Entry(m, 10)
    entry.draw(win)

    while True:
        key = win.getKey()
        if key == "Return": break
    entry.undraw()
    typed = entry.getText()
    Text(m, typed).draw(win)

    win.checkMouse()

def gui():
    win = GraphWin("", 500, 500)

    while True:
        key = win.checkKey()

        if key == "q":
            break
        if key:
            handle_key(win, key)

        m = win.checkMouse()
        if m:
            check_mouse(win, m)
    win.close()

gui()