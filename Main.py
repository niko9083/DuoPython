import pygame
from Classes import svarBox
svarBoxes = []
import time

pygame.init()

windowWidth = 1080
windowHeight = 760
clock = pygame.time.Clock()
screen = pygame.display.set_mode((windowWidth, windowHeight))

titleFont = pygame.font.SysFont("Arial", 100, True)
font = pygame.font.SysFont("Arial", 50)
sponsorFont = pygame.font.SysFont("Arial", 20)

def mainMenu():
    global done
    done = False
    levels = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                done = True
                continue

            screen = pygame.display.set_mode((windowWidth, windowHeight))
            screen.fill((0, 0, 0))

            mouseX, mouseY = pygame.mouse.get_pos()
            mouseText = sponsorFont.render(f"{mouseX} ; {mouseY}", False, (255, 255, 255))
            screen.blit(mouseText, (0, windowHeight-20))

            titleText = titleFont.render("DuoPython", False, (255, 255, 255))

            # Level select button
            if mouseX <= 245 and 210 >= mouseY >= 150:
                levelSelectText = font.render(" Level Select ", False, (0, 0, 0), (255, 255, 255))
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    levels = not levels
            else:
                levelSelectText = font.render(" Level Select ", False, (255, 255, 255))

            if levels:
                # If statement button
                if 300 <= mouseX <= 545 and 150 <= mouseY <= 200:
                    ifs = font.render(" If statemens ", False, (0, 0, 0), (255, 255, 255))
                else:
                    ifs = font.render(" If statemens ", False, (255, 255, 255))

                # For loops button
                if 300 <= mouseX <= 495 and 225 <= mouseY <= 275:
                    fors = font.render(" For loops ", False, (0, 0, 0), (255, 255, 255))
                else:
                    fors = font.render(" For loops ", False, (255, 255, 255))

                # While loops button
                if 300 <= mouseX <= 535 and 300 <= mouseY <= 350:
                    whiles = font.render(" While loops ", False, (0, 0, 0), (255, 255, 255))
                else:
                    whiles = font.render(" While loops ", False, (255, 255, 255))

                screen.blit(ifs, (300, 150))
                screen.blit(fors, (300, 225))
                screen.blit(whiles, (300, 300))

            # Quit button
            if mouseX <= 120 and 285 >= mouseY > 225:
                quitText = font.render(" QUIT ", False, (0, 0, 0), (255, 255, 255))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    done = True
                    continue
            else:
                quitText = font.render(" QUIT ", False, (255, 255, 255))

            screen.blit(titleText, (0, 0))
            screen.blit(levelSelectText, (0, 150))
            screen.blit(quitText, (0, 225))

            pygame.display.flip()
            clock.tick(60)

mainMenu()
