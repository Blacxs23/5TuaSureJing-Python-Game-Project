import pygame
from pygame import mixer

mixer.init()

#load music snd sonds
pygame.mixer.music.load("")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
