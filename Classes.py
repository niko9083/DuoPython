import pygame

class svarBox:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.width = 100
        self.height =69
        self.color = (255, 255, 255)
        self.theScreen = screen
    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
    def isMouseOver(self, mouseX, mouseY):
        if mouseX>self.x and mouseX< self.x + self.width and mouseY>self.y and mouseY<self.y + self.height:
            return True
        else:
            return False


