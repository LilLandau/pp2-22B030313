import pygame
from random import randrange

WIDTH = 800
HEIGHT = 700
BLOCK_SIZE = 50
FPS = 5

#начальные координаты змейки и еды
x, y = randrange(0, WIDTH, BLOCK_SIZE), randrange(0, HEIGHT, BLOCK_SIZE)
food = randrange(0, WIDTH, BLOCK_SIZE), randrange(0, HEIGHT, BLOCK_SIZE)


#параметры змейки
len_snake = 1
snake = [(x, y)]
dx, dy = 0, 0

pygame.init()

#параметры игры
font = pygame.font.SysFont('Verdana', 20)
score = 0
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake_game")
clock = pygame.time.Clock()

running = True
while running:
    SCREEN.fill((0, 0, 0))

    #счетчики
    score_rendered = font.render(f"score: {score}", True, (255, 255, 255))
    SCREEN.blit(score_rendered, (10, 10))
    level_rendered = font.render(f"level: {score // 5}", True, (255, 255, 255))
    SCREEN.blit(level_rendered, (WIDTH-120, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #рисую змейку
    for i, j in snake:
        pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            pygame.Rect(i, j, BLOCK_SIZE, BLOCK_SIZE)
        )    

    #движение змейки
    x += dx * BLOCK_SIZE
    y += dy * BLOCK_SIZE
    snake.append((x, y))
    snake = snake[-len_snake:]

    #столкновение еды и змейки
    if snake[-1] == food:
        food = randrange(0, WIDTH, BLOCK_SIZE), randrange(0, HEIGHT, BLOCK_SIZE)    #респавн яблока
        len_snake += 1
        score += 1

    #управление змейкой
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        dx, dy = 0, -1
    if pressed[pygame.K_DOWN]:
        dx, dy = 0, 1
    if pressed[pygame.K_LEFT]:
        dx, dy = -1, 0
    if pressed[pygame.K_RIGHT]:
        dx, dy = 1, 0        

    #рисую еду
    pygame.draw.rect(
        SCREEN,
        (255, 0, 00),
        (*food, BLOCK_SIZE, BLOCK_SIZE)
    )

    #выход за края
    if x < 0 or x > WIDTH - BLOCK_SIZE: running = False
    if y < 0 or y > HEIGHT - BLOCK_SIZE: running = False

    #змейка ест саму себя
    if len(snake) != len(set(snake)): running = False

    pygame.display.update()
    #ускорение игры с повышением уровня
    clock.tick(FPS + (score // 5)*2)