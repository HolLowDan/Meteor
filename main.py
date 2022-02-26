import pygame, random, sys
from pygame.locals import *


def close_game():
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                close_game()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Нажатие ESC осуществляет выход.
                    close_game()
            return


def playerHasgivesnowball(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

