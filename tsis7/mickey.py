import pygame
import sys
import datetime

pygame.init()
screen = pygame.display.set_mode((700, 700))

fps = pygame.time.Clock()

clock = pygame.image.load("clock.png")
clock_rect = clock.get_rect()
clock_rect.center = (350, 350)  #центр относительно дисплея

minute = pygame.image.load("minute.png")
w_minute, h_minute = minute.get_size()
minute_angle = datetime.datetime.now().minute*10
minute_rect = minute.get_rect()
minute_rect.center = (350, 350-h_minute/2)

second = pygame.image.load("second.png")
w_second, h_second = second.get_size()
second_angle = datetime.datetime.now().second*6


def blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
  


while True:
    fps.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pos = (screen.get_width()/2, screen.get_height()/2)
    press = pygame.key.get_pressed()

    screen.fill((255, 255, 255))
    screen.blit(clock, clock_rect)

    blitRotate(screen, second, pos, (w_second/2, h_second), second_angle)
    second_angle -= 6
    
    blitRotate(screen, minute, pos, (w_minute/2, h_minute), minute_angle)
    minute_angle -= 0.1

    pygame.display.flip()
