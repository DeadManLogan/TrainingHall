from poker_app import PokerApp
from poker_interface import TextInterface, GraphicsInterface

def main():
    inter = GraphicsInterface()
    app = PokerApp(inter)
    app.run()

if __name__ == "__main__":
    main()