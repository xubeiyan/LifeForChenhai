#-*-coding:utf-8-*-

import pygame, sys
from pygame.locals import *

#开始？
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Life for Chenhai")

#load bitmaps
producer = pygame.image.load("images\MSRClogo.png").convert_alpha()

#repeating loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		sys.exit()
	#draw background
	screen.blit(producer, (0, 0))

	pygame.display.update()
	