import random
import sys

import pygame
from pygame.locals import *


def terminate():
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # pressing escape quits
                    terminate()
                return


def playerHasHitRock(playerRect, rock):
    for b in rock:
        if playerRect.colliderect(b['rect']):
            return True
    return False


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
FPS = 60
ROCKMINSIZE = 10
ROCKMAXSIZE = 40
ROCKMINSPEED = 1
ROCKMAXSPEED = 8
ADDNEWROCKRATE = 6
PLAYERMOVERATE = 5

