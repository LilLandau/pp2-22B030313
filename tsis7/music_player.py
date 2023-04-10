#создать треклист
#включить 0 трек
#реализовать функционал (выкл, стоп, продолжить, пред, послед)

import pygame
import os
import time

os.chdir(r'C:\Users\Landau\Desktop\tsis7\playlist')                 #переход в директорию с музыкой
song_list = os.listdir(r'C:\Users\Landau\Desktop\tsis7\playlist')   #трек-лист
index = 0

pygame.init()
screen = pygame.display.set_mode((200, 200))
pygame.mixer.music.set_volume(1.0)              
for song in song_list:                  #автопроигрыш
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(0)
clock = pygame.time.Clock()

def play_next_song():
    global song_list
    global index

    #порядок воспроизведения
    if index + 1 >= len(song_list): index = 0
    else: index += 1

    pygame.mixer.music.load(song_list[index])
    pygame.mixer.music.play(0)

def play_previous_song():
    global song_list
    global index

    #порядок воспроизведения
    if index == 0: index = 2
    else: index -= 1

    pygame.mixer.music.load(song_list[index])
    pygame.mixer.music.play(0)
    
done = False

while not done:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        pygame.mixer.music.pause()
        print("Song is paused")
        time.sleep(0.5)
    if pressed[pygame.K_DOWN]:
        pygame.mixer.music.unpause()
        time.sleep(0.5)
        print("Song is resumed")
    if pressed[pygame.K_RIGHT]:
        play_next_song()
        time.sleep(0.5)
        print("Next song is playing")
    if pressed[pygame.K_LEFT]:
        play_previous_song()
        time.sleep(0.5)
        print("Previous song is playing")
    if pressed[pygame.K_ESCAPE]:
        pygame.mixer.music.stop()
        print("Playing is over")
        break                             
        

    pygame.display.flip()
    clock.tick(24)