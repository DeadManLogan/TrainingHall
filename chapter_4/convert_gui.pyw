from graphics import *

def temp_conversion():
    win = GraphWin('Temperature', 500, 500)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    Text(Point(1, 3), 'Celsius: ').draw(win)
    Text(Point(1, 3.2), 'Fahrenheit: ').draw(win)

    inputText = Entry(Point(2.25, 3), 5)
    inputText.setText('0.0')
    inputText.draw(win)

    outputText = Entry(Point(2.5, 1), 6)
    outputText.draw(win)

    button = Text(Point(1.5, 2.0), 'Convert It')
    button.draw(win)

    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

    win.getMouse()

    celsius = float(inputText.getText())
    fahrenheit = 9.0/5.0 * celsius + 32
    outputText.setText(fahrenheit)
    button.setText('Quit')

    win.getMouse()
    win.close()

temp_conversion()