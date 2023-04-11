import pygame

pygame.init()
screen = pygame.display.set_mode((800, 640))
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

rect_text = font.render("Rect", True, WHITE)
circle_text = font.render("Circ", True, WHITE)
square_text = font.render("Sq", True, WHITE)
r_triangle_text = font.render("RTrig", True, WHITE)
eq_triangle_text = font.render("EQTrig", True, WHITE)
rhombus_text = font.render("Rhom", True, WHITE)

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
        screen.blit(square_text, (200, 5))
        screen.blit(r_triangle_text, (290, 5))
        screen.blit(eq_triangle_text, (350, 5))
        screen.blit(rhombus_text, (440, 5))

        screen.blit(eraser_text, (540, 5))
        screen.blit(red_text, (600, 5))
        screen.blit(green_text, (660, 5))
        screen.blit(blue_text, (720, 5))

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            if 10 <= x_mouse < 130 and y_mouse <= 40:
                shape = 'rect' #select rect
            if 130 <= x_mouse < 200 and y_mouse <= 40:
                shape = 'circle' #select circle



            if 200 <= x_mouse < 290 and y_mouse <= 40:
                shape = 'square' 
            if 290 <= x_mouse < 350 and y_mouse <= 40:
                shape = 'r_trinagle' 
            if  350 <= x_mouse < 440 and y_mouse <= 40:
                shape = 'eq_triangle'
            if 440 <= x_mouse < 540 and y_mouse <= 40:
                shape = 'rhombus'

            if 540 <= x_mouse < 600 and y_mouse <= 40:
                color = 'eraser' 
            if 600 <= x_mouse < 660 and y_mouse <= 40:
                color = 'red' 
            if  600 <= x_mouse < 720 and y_mouse <= 40:
                color = 'green'
            if 720 <= x_mouse < 800 and y_mouse <= 40:
                color = 'blue'

        if event.type == pygame.MOUSEMOTION:
            if shape == 'rect':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen, WHITE, [x_mouse, y_mouse, 15, 25], 0)
                
            if shape == 'rect' and color == 'eraser':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen, WHITE, [x_mouse, y_mouse, 15, 25], 0)

            if shape == 'rect' and color == 'red':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen, RED, [x_mouse, y_mouse, 15, 25], 0)

            if shape == 'rect' and color == 'green':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen, GREEN, [x_mouse, y_mouse, 15, 25], 0)

            if shape == 'rect' and color == 'blue':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen, BLUE, [x_mouse, y_mouse, 15, 25], 0)



            if shape == 'circle':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen, WHITE, (x_mouse, y_mouse), 15, 0)
            
            if shape == 'circle' and color == 'eraser':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen, WHITE, (x_mouse, y_mouse), 15, 0)

            if shape == 'circle' and color == 'red':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen, RED, (x_mouse, y_mouse), 15,0)

            if shape == 'circle' and color == 'green':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen, GREEN, (x_mouse, y_mouse), 15, 0)

            if shape == 'circle' and color == 'blue':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen, BLUE, (x_mouse, y_mouse), 15, 0)



            if shape == 'square':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen, WHITE, [x_mouse, y_mouse, 25, 25], 0)
                
            if shape == 'square' and color == 'eraser':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen, WHITE, [x_mouse, y_mouse, 25, 25], 0)

            if shape == 'square' and color == 'red':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen, RED, [x_mouse, y_mouse, 25, 25], 0)

            if shape == 'square' and color == 'green':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen, GREEN, [x_mouse, y_mouse, 25, 25], 0)

            if shape == 'square' and color == 'blue':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen, BLUE, [x_mouse, y_mouse, 25, 25], 0)



            if shape == 'r_trinagle':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, WHITE, ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)

            if shape == 'r_trinagle' and color == 'eraser':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, WHITE, ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)


            if shape == 'r_trinagle' and color == 'red':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, RED, ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)


            if shape == 'r_trinagle' and color == 'green':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, GREEN, ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)


            if shape == 'r_trinagle' and color == 'blue':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, BLUE, ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)





            if shape == 'eq_triangle':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, WHITE, ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)

            if shape == 'eq_triangle' and color == 'eraser':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, WHITE, ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)


            if shape == 'eq_triangle' and color == 'red':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, RED, ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)


            if shape == 'eq_triangle' and color == 'green':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, GREEN, ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)


            if shape == 'eq_triangle' and color == 'blue':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, BLUE, ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)



            if shape == 'rhombus':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, WHITE, ((x_mouse, y_mouse), (x_mouse+20, y_mouse-20), (x_mouse+40, y_mouse), (x_mouse+20, y_mouse+20)))

            if shape == 'rhombus' and color == 'eraser':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, WHITE, ((x_mouse, y_mouse), (x_mouse+20, y_mouse-20), (x_mouse+40, y_mouse), (x_mouse+20, y_mouse+20)))


            if shape == 'rhombus' and color == 'red':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, RED, ((x_mouse, y_mouse), (x_mouse+20, y_mouse-20), (x_mouse+40, y_mouse), (x_mouse+20, y_mouse+20)))


            if shape == 'rhombus' and color == 'green':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, GREEN, ((x_mouse, y_mouse), (x_mouse+20, y_mouse-20), (x_mouse+40, y_mouse), (x_mouse+20, y_mouse+20)))


            if shape == 'rhombus' and color == 'blue':
                x_mouse, y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, BLUE, ((x_mouse, y_mouse), (x_mouse+20, y_mouse-20), (x_mouse+40, y_mouse), (x_mouse+20, y_mouse+20)))





        pygame.display.flip()
        clock.tick(60)
