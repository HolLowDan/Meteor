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


def playerHashitrock(playerRect, rock):
    for b in rock:
        if playerRect.colliderect(b['rect']):
            return True
    return False


if __name__ == '__main__':
    pygame.init()
    mainClock = pygame.time.Clock()
    rock = []
    FPS = 60
    WINDOWWIDTH, WINDOWHEIGHT = 1000, 600
    ROCKMINSIZE, ROCKMAXSIZE = 15, 25
    ROCKMINSPEED, ROCKMAXSPEED = 3, 5
    ADDNEWROCKRATE = 6
    rockAddCounter = 0
    PLAYERMOVERATE = 5
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
    rockImage = pygame.image.load('Image/rock.png')
    backgraudImage = pygame.image.load("Image/background.jpg").convert()
    backgraudImage = pygame.transform.smoothscale(backgraudImage, screen.get_size())

    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = False
    RockAddCounter = 3
    SnowballAddCounter = 5

    pygame.mixer.music.play(-1, 0.0)
    screen.blit(backgraudImage, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                close_game()

            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    close_game()

                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False

        if rockAddCounter == ADDNEWROCKRATE:
            rockAddCounter = 0
            rockSize = random.randint(ROCKMINSIZE, ROCKMAXSIZE)
            newRock = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - rockSize), 0 - rockSize, rockSize, rockSize),
                         'speed': random.randint(ROCKMINSPEED, ROCKMAXSPEED),
                         'surface': pygame.transform.scale(rockImage, (rockSize, rockSize)),
                        }
            rock.append(newRock)
        else:
            rockAddCounter += 1

        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)

        for b in rock:
            b['rect'].move_ip(0, b['speed'])

        for b in rock[:]:
            if b['rect'].top > WINDOWHEIGHT:
                rock.remove(b)

        for b in rock:
            screen.blit(b['surface'], b['rect'])
        screen.blit(playerImage, playerRect)

        if playerHashitrock(playerRect, rock):
            break

        pygame.display.update()
        mainClock.tick(FPS)
