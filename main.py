from display import Display
from game import Game
from config import *


class Main(object):
    def __init__(self):
        # Display() is responsible for handling front-end
        # Game() is responsible for handling back-end
        self.display = Display()
        self.game = Game()
        # self.run() is the main function of the Main() class, inside happens everything
        self.run()

    def run(self):
        while True:
            self.game.tick()
            self.display.draw()


if __name__ == "__main__":
    Main()
