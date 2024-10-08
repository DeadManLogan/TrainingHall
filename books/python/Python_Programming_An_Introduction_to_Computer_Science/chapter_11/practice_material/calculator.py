from graphics import *
from button import Button

class Calculator:
    def __init__(self):
        win = GraphWin("Calculator")
        win.setCoords(0, 0, 6, 7)
        win.setBackground("slategray")
        self.win = win
        self.__create_buttons()
        self.__create_display()

    def __create_buttons(self):
        button_specs = [(2, 1, '0'), (3, 1, '.'),
                        (1, 2, '1'), (2, 2, '2'), (3, 2, '3'),
                        (4, 2, '+'), (5, 2, '-'), (1, 3, '4'),
                        (2, 3, '5'), (3, 3, '6'), (4, 3, '*'),
                        (5, 3, '/'), (1, 4, '7'), (2, 4, '8'),
                        (3, 4, '9'), (4, 4, '<-'), (5, 4, 'C')]
        self.buttons = []

        for (cx, cy, label) in button_specs:
            self.buttons.append(Button(self.win, Point(cx, cy), .75, .75, label))
        self.buttons.append(Button(self.win, Point(4.5, 1), 1.75, .75, '='))
        for b in self.buttons:
            b.activate()

    def __create_display(self):
        bg = Rectangle(Point(.5, 5.5), Point(5.5, 6.5))
        bg.setFill("white")
        bg.draw(self.win)
        text = Text(Point(3, 6), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(16)
        self.display = text

    def run(self):
        while True:
            key = self.get_key_press()
            self.process_key(key)

    def get_key_press(self):
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.get_label()
                
    def process_key(self, key):
        text = self.display.getText()
        if key == "C":
            self.display.setText("")
        elif key == "<-":
            self.display.setText(text[:-1])
        elif key == "=":
            try:
                result = eval(text)
            except:
                result = "ERROR"
            self.display.setText(str(result))
        else:
            self.display.setText(text + key)

def main():
    calculator = Calculator()
    calculator.run()

if __name__ == "__main__":
    main()