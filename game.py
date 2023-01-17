import graphics
import pygame
from config import *
import sys


class Game(object):
    def __init__(self, main):
        self.main = main
        self.fps = FPS
        self.clock = pygame.time.Clock()
        self.stage = "launch_screen"
        self.simulation_subobject = None

    def tick(self, *objects):
        self.handle_events()
        for obj in objects:
            obj.tick()
        self.clock.tick(self.fps)

    def handle_MBD(self, pos):
        rects = self.main.display.current_rects
        match self.stage:
            case "launch_screen":
                for i in range(len(rects)):
                    if rects[i].collidepoint(pos):
                        match i:
                            case 1:
                                self.change_stage(stage="throw")
                            case 2:
                                self.change_stage(stage="gravity_points")

    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    sys.exit(0)
                case pygame.KEYDOWN:
                    # \/ Handle keyboard input
                    match event.key:
                        case pygame.K_ESCAPE:
                            sys.exit(0)
                case pygame.MOUSEBUTTONDOWN:
                    self.handle_MBD(pygame.mouse.get_pos())

    def change_stage(self, stage):
        match stage:
            case "launch_screen":
                self.stage = "launch_screen"
            case "throw":
                self.stage = "throw"
                self.simulation_subobject
            case "gravity_points":
                self.stage = "throw"
                self.simulation_subobject
