import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

radius = 15
x = 0
y = 0
mode = 'blue'
points = []

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont('Verdana', 20)
rect_text = font.render("Rectangle", True, WHITE)
circle_text = font.render("Cicrle", True, WHITE)
eraser_text = font.render("Eraser", True, WHITE)
red_text = font.render("red", True, RED)
green_text = font.render("green", True, GREEN)
blue_text = font.render("blue", True, BLUE)

running = True
shape = ""
color = ""
screen.fill((255, 255, 255))


while running:
    for event in pygame.event.get():

        pygame.draw.rect(screen, BLACK, (0, 0, 640, 40))
        screen.blit(rect_text, (10, 5))
        screen.blit(circle_text, (130, 5))
        screen.blit(eraser_text, (200, 5))
        screen.blit(red_text, (290, 5))
        screen.blit(green_text, (350, 5))
        screen.blit(blue_text, (440, 5))

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            if 10 <= x_mouse < 130 and y_mouse <= 40:
                shape = 'rect' #select rect
            if 130 <= x_mouse < 200 and y_mouse <= 40:
                shape = 'circle' #select circle
            if 200 <= x_mouse < 290 and y_mouse <= 40:
                color = 'eraser' #eraser
            if 290 <= x_mouse < 350 and y_mouse <= 40:
                color = 'red' 
            if  350 <= x_mouse < 440 and y_mouse <= 40:
                color = 'green'
            if 440 <= x_mouse < 540 and y_mouse <= 40:
                color = 'blue'

        if event.type == pygame.MOUSEMOTION:
            if shape == 'rect':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(
                    screen, 
                    WHITE, 
                    [x_mouse, y_mouse, 15, 25], 
                    0
                    )
                
            if shape == 'rect' and color == 'eraser':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(
                    screen, 
                    WHITE, 
                    [x_mouse, y_mouse, 15, 25], 
                    0
                    )

            if shape == 'rect' and color == 'red':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(
                    screen, 
                    RED, 
                    [x_mouse, y_mouse, 15, 25], 
                    0
                    )

            if shape == 'rect' and color == 'green':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(
                    screen, 
                    GREEN, 
                    [x_mouse, y_mouse, 15, 25], 
                    0
                    )

            if shape == 'rect' and color == 'blue':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(
                    screen, 
                    BLUE, 
                    [x_mouse, y_mouse, 15, 25], 
                    0
                    )

            if shape == 'circle':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(
                    screen, 
                    WHITE, 
                    (x_mouse, y_mouse), 
                    15,
                    0
                    )
            
            if shape == 'circle' and color == 'eraser':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(
                    screen, 
                    WHITE, 
                    (x_mouse, y_mouse), 
                    15,
                    0
                    )

            if shape == 'circle' and color == 'red':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(
                    screen, 
                    RED, 
                    (x_mouse, y_mouse), 
                    15,
                    0
                    )

            if shape == 'circle' and color == 'green':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(
                    screen, 
                    GREEN, 
                    (x_mouse, y_mouse), 
                    15,
                    0
                    )

            if shape == 'circle' and color == 'blue':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(
                    screen, 
                    BLUE, 
                    (x_mouse, y_mouse), 
                    15,
                    0
                    )


        pygame.display.flip()
        clock.tick(60)