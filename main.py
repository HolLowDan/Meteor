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


def playerHasgivesnowball(playerRect, Snowball):
    for b in Snowball:
        if playerRect.colliderect(b['rect']):
            return True
    return False


def playerHashitstone(playerRect, Stone):
    for b in Stone:
        if playerRect.colliderect(b['rect']):
            return True
    return False


