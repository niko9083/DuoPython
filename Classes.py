import pygame

class svarBox:
    def __init__(self, x, y, width, heigth, screen):
        self.x = x
        self.y = y
        self.width = 10
        self.heigth =7
        self.color = (255 , 255, 255)
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
