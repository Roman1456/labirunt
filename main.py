import pygame
from pygame import *
from Player import Player
from Player1 import Peri
from Walld import Wall


window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

backround = pygame.transform.scale(
    pygame.image.load("kartka/.png"),(700,500)
)

niger = Player(626,425,50,50, "kartka/images.jpg", 10,50)
peri = Peri(40,0,50,50, "kartka/images.png", 10)

walls = []
walls.append(Wall(100,0,700,20))
walls.append(Wall(680,0,30,600))
walls.append(Wall(0,480,600,20))
walls.append(Wall(0,0,30,600))
walls.append(Wall(540,390,150,20))
walls.append(Wall(20,300,100,20))







game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

        if event.type == pygame.QUIT:
            pygame.quit()

    for wall in walls:
        if wall.rect.colliderect(peri.hitbox):
            game = False








    window.blit(backround, (0, 0))
    for wall in walls:
        wall.draw(window)
    peri.move()
    #niger.move()
    peri.draw(window)
    niger.draw(window)
    pygame.display.flip()
    fps.tick(60)