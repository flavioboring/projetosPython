#exercicio 24
#Faça um programa que abre e reproduza um áudio e um arquivo MP3
import pygame
pygame.init()
pygame.mixer.music.load(('sultansofswing.mp3'))
pygame.mixer.music.play()
pygame.event.wait()
