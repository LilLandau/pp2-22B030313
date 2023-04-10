import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
fps = pygame.time.Clock()
done = False
x = screen.get_size()[0]/2
y = screen.get_size()[1]/2
speed = 20

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 25: y -= speed
    if pressed[pygame.K_DOWN] and y < screen.get_size()[1] - 50: y += speed
    if pressed[pygame.K_LEFT] and x > 25: x -= speed
    if pressed[pygame.K_RIGHT] and x < screen.get_size()[0] - 25: x += speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.flip()
    fps.tick(120)