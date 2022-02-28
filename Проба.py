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
                if event.key == K_ESCAPE:  # кнопка выхода
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


# Начинаем игру
pygame.init()
mainClock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Метеор')
pygame.mouse.set_visible(False)


# Добовляем шрифт
font = pygame.font.SysFont(None, 48)


# Добовляем музыку
gameOverSound = pygame.mixer.Sound('Sound/zvuki-quotkonets-igryiquot-game-over-sounds-30249.ogg')
pygame.mixer.music.load('Sound/Mathias Rehfeldt Dark Matter Projekt - Ice Field.mp4')


# Добовляем картинки
playerImage = pygame.image.load('Image/character.png')
playerRect = playerImage.get_rect()
rockImage = pygame.image.load('Image/rock.png')
backgroudImage = pygame.image.load("Image/background.jpg").convert()
backgroudImage = pygame.transform.smoothscale(backgroudImage, screen.get_size())


# покащываем стартовый экран
drawText('Метеор', font, screen, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Нажмите для начала', font, screen, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()


topScore = 0
while True:
    # начинаем игру
    rock = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 100)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    rockAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)