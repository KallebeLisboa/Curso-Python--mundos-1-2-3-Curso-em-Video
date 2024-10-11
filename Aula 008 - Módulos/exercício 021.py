# Faça um programa de python que abra e 
# reproduza um arquivo Mp3 #

import pygame
pygame.init()
pygame.mixer.music.load('Odisseia, um novo final.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
