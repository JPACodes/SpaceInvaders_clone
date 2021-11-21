import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1600, 880))

# Title and Icon
pygame.display.set_caption("Astro Movers")
icon = pygame.image.load('jpalogolarge.jpg')
pygame.display.set_icon(icon)
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        # pygame.quit is checking if the close button is clicked
        if event.type == pygame.QUIT:
            running = False
    # anything continuous needs to be inside loop
    screen.fill((68, 0, 139))
    pygame.display.update()
