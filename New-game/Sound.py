import pygame
from pygame import mixer

mixer.init()

#load music and set volume
pygame.mixer.music.load("New-game/asset/sound/music1.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

pygame.mixer.music.load("New-game/asset/sound/musiclobby.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

pygame.mixer.music.load("New-game/asset/sound/music3.mp3")
pygame.mixer.music.set_volume(0.5) 
pygame.mixer.music.play(-1, 0.0, 5000)

#play attack and take hit sounds
punch1_sound = mixer.Sound("New-game/asset/sound/punch1.wav")
punch1_sound.set_volume(0.3)
punch2_sound = mixer.Sound("New-game/asset/sound/punch2.wav")
punch2_sound.set_volume(0.3)

takehit1_sound = mixer.Sound("New-game/asset/sound/takehit.wav")
takehit1_sound.set_volume(0.3)
takehit2_sound = mixer.Sound("New-game/asset/sound/takehit2.wav")
takehit2_sound.set_volume(0.3)

dead_sound1 = mixer.Sound("New-game/asset/sound/dead1.wav")
dead_sound1.set_volume(0.3)
dead_sound2 = mixer.Sound("New-game/asset/sound/dead2.wav")
dead_sound2.set_volume(0.3)


