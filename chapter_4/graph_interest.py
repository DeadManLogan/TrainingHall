from graphics import *

def principal_graph():
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

def tic_tac_toe():
    win = GraphWin()
    win.setCoords(0.0, 0.0, 3.0, 3.0)

    Line(Point(1, 0), Point(1,3)).draw(win)
    Line(Point(2, 0), Point(2,3)).draw(win)

    Line(Point(0, 1), Point(3, 1)).draw(win)
    Line(Point(0, 2), Point(3, 2)).draw(win)

    close_win = int(input("Close"))

def show_mouse_clicks():
    win = GraphWin()
    for i in range(10):
        p = win.getMouse()
        print(p)

def draw_triangle():
    win = GraphWin()
    win.setCoords(0, 0, 10, 10)
    message = Text(Point(5, 0.5), 'Click three points to make a triangle')
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    tri = Polygon(p1, p2, p3)
    tri.setFill('peachpuff')
    tri.setOutline('cyan')
    tri.draw(win)

    message.setText("Click anywhere to quit.")
    win.getMouse()

draw_triangle()