from config import *
from graphics import Graphics


class Display(object):
    def __init__(self, main):
        # Config
        self.name = "Physics Engine"
        # Init
        self.main = main
        self.size = pygame.math.Vector2(WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.name)
        self.current_rects = []

    def draw(self, stage, *objects):
        self.screen.fill(black)
        match stage:
            case "launch_screen":
                self.draw_launch_screen()
        draw_objects(*objects)
        pygame.display.flip()

    def draw_launch_screen(self):
        Graphics.launch_screen.choose_mode(screen=self.screen)
        self.current_rects.append(Graphics.launch_screen.choose_mode(screen=self.screen, mode="get_rect"))
        Graphics.launch_screen.throw(screen=self.screen)
        self.current_rects.append(Graphics.launch_screen.throw(screen=self.screen, mode="throw"))
        Graphics.launch_screen.gravity_points(screen=self.screen)
        self.current_rects.append(Graphics.launch_screen.gravity_points(screen=self.screen, mode="gravity_points"))


def draw_objects(*objects):
    for obj in objects:
        obj.draw()
