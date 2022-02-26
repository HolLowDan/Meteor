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


def playerHasgivesnowball(playerRect, snowball):
    for b in snowball:
        if playerRect.colliderect(b['rect']):
            return True
    return False


def playerHashitstone(playerRect, stone):
    for b in stone:
        if playerRect.colliderect(b['rect']):
            return True
    return False


if __name__ == '__main__':
    pygame.init()
    WINDOWWIDTH, WINDOWHEIGHT = 1000, 600
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Снежный ком')
    pygame.mouse.set_visible(False)

    # шрифт
    font = pygame.font.SysFont(None, 48)

    # звуки
    gameOverSound = pygame.mixer.Sound('Sound/zvuki-quotkonets-igryiquot-game-over-sounds-30249.ogg')
    pygame.mixer.music.load('Sound/Mathias Rehfeldt Dark Matter Projekt - Ice Field.mp4')

    #  Image
    playerImage = pygame.image.load('Image/character.png')
    playerRect = playerImage.get_rect()
    snowballImage = pygame.image.load('Image/snow-ball.png')
    backgraudImage = pygame.image.load("Image/background.jpg").convert()
    backgraudImage = pygame.transform.smoothscale(backgraudImage, screen.get_size())

    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    screen.blit(backgraudImage, (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    close_game()
