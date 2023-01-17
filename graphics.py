from config import *
from pygame.math import Vector2

class Set_Of_Graphics(object):
    def __init__(self):
        self.launch_screen = Launch_Screen()


class Launch_Screen(object):
    def choose_mode(self, screen, mode="draw"):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Choose mode:", True, white, None)  # text, antialiasing, color, background
        left_top = pygame.math.Vector2(100, 100)

        text_rect = text.get_rect()
        text_rect.topleft = left_top
        if mode == "draw":
            screen.blit(text, text_rect)

    def throw(self, screen, mode="draw"):
        font = pygame.font.Font('freesansbold.ttf', 26)
        text = font.render("Throw", True, white, None)  # text, antialiasing, color, background
        left_top = pygame.math.Vector2(150, 160)

        text_rect = text.get_rect()
        text_rect.topleft = left_top
        if mode == "draw":
            screen.blit(text, text_rect)
        if mode == "get_rect":
            return text_rect

    def gravity_points(self, screen, mode="draw"):
        font = pygame.font.Font('freesansbold.ttf', 26)
        text = font.render("Gravity simulation with mass points", True, white, None)
        # text, antialiasing, color, background
        left_top = pygame.math.Vector2(150, 220)

        text_rect = text.get_rect()
        text_rect.topleft = left_top
        if mode == "draw":
            screen.blit(text, text_rect)
        if mode == "get_rect":
            return text_rect


Graphics = Set_Of_Graphics()
