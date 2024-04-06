import pygame
from pygame import *
from Player import Player
from Player1 import Peri



window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

backround = pygame.transform.scale(
    pygame.image.load("kartka/download.jpg"),(700,500)
)

niger = Player(100,100,50,50, "kartka/images.jpg", 10)
peri = Peri(150,200,50,50, "kartka/images.png", 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()












    window.blit(backround, (0, 0))
    peri.move()
    peri.draw(window)
    niger.draw(window)
    pygame.display.flip()
    fps.tick(60)