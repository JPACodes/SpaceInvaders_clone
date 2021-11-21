import pygame
import random

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Astro Movers")
icon = pygame.image.load('jpalogolarge.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('battleship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0,760)
enemyY = random.randint(50,120)
enemyX_change = random.uniform(0.1, 0.3)

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True

while running:
    screen.fill((68, 0, 139))

    for event in pygame.event.get():
        # pygame.quit is checking if the close button is clicked
        if event.type == pygame.QUIT:
            running = False
        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
                print("Right arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("Keystroke is lifted")

    # anything continuous needs to be inside loop
    # call player AFTER screen.fill because the screen is drawn first
    # 5 = 5 + -0.1 -> 5 = 5 - 0 . 1
    # 5 = 5 + 0.1
    playerX += playerX_change
    enemyX += enemyX_change
    if enemyX <=0:
        enemyX = 0
        enemyX_change = random.uniform(0.1, 0.5)
    elif enemyX >= 736:
        enemyX = 736
        enemyX_change = -random.uniform(0.1, 0.5)

    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
