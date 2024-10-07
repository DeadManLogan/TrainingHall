from poker_app import PokerApp
from poker_interface import TextInterface

def main():
    inter = TextInterface()
    app = PokerApp(inter)
    app.run()

if __name__ == "__main__":
    main()