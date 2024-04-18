import pygame
from pygame import *
from Player import Player
from Player1 import Peri
from Walld import Wall


window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

backround = pygame.transform.scale(
    pygame.image.load("kartka/labirint.png"),(700,500)
)

niger = Player(626,425,50,50, "kartka/images.jpg", 10,50)
peri = Peri(40,0,50,50, "kartka/images.png", 10)

walls = []
walls.append(Wall(100,0,700,60))
walls.append(Wall(675,0,30,600))
walls.append(Wall(0,440,610,60))
walls.append(Wall(0,0,30,600))
walls.append(Wall(220,60,15,165))
walls.append(Wall(95,210,200,15))
walls.append(Wall(95,140,70,15))
walls.append(Wall(95,140,15,80))
walls.append(Wall(30,285,60,15))
walls.append(Wall(155,220,15,70))
walls.append(Wall(280,220,15,75))
walls.append(Wall(220,280,70,15))
walls.append(Wall(220,280,15,70))



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