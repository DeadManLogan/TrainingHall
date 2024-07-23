from graphics import *

print("This code will claculate and show in a diagram, the progess of an investment in 10-years.")
principal = float(input("Enter the amount you want to invest: "))
apr = float(input("Enter the interest rate: "))

win = GraphWin('Investment', 400, 400)

label = ['0k', '2k', '4k', '8k', '10k']
v_label = 390
for i in label:
    Text(Point(20, v_label), i).draw(win)
    v_label -= 50

first_bar = Rectangle(Point(40, 390), Point(65, 390 - (principal*0.02)))
first_bar.setFill('green')
first_bar.draw(win)

for year in range(1, 11):
    principal += principal*apr
    x_start_point = 25*year + 40
    bar_height = principal*0.02
    bar = Rectangle(Point(x_start_point, 390), Point(x_start_point + 25, 390 - bar_height))
    bar.setFill('green')
    bar.draw(win)

close_win = int(input("Close"))