import pygame
from pygame import *
from Player import Player
from Player1 import Peri
from Walld import Wall


window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

backround = pygame.transform.scale(
    pygame.image.load("kartka/download.jpg"),(700,500)
)

niger = Player(400,100,50,50, "kartka/images.jpg", 10,50)
peri = Peri(40,23,50,50, "kartka/images.png", 10)

walls = []
walls.append(Wall(100,1,30,100))
walls.append(Wall(100,90,100,20))
walls.append(Wall(100,175,30,100))



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