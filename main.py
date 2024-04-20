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

niger = Player(626,425,50,50, "kartka/images.jpg", 10,50)
peri = Peri(40,0,40,40, "kartka/images.png", 10)

walls = []
walls.append(Wall(100,0,700,60))
walls.append(Wall(675,0,30,600))
walls.append(Wall(0,440,610,60))
walls.append(Wall(0,0,30,600))
walls.append(Wall(220,60,10,160))
walls.append(Wall(95,210,195,10))
walls.append(Wall(95,140,70,10))
walls.append(Wall(95,140,10,80))
walls.append(Wall(30,285,60,10))
walls.append(Wall(155,220,10,70))
walls.append(Wall(280,220,10,70))
walls.append(Wall(220,280,70,10))
walls.append(Wall(220,280,10,80))
walls.append(Wall(105,350,125,10))
walls.append(Wall(285,370,10,100))
walls.append(Wall(410,60,10,80))
walls.append(Wall(410,350,10,100))
walls.append(Wall(350,350,130,10))
walls.append(Wall(350,300,10,50))
walls.append(Wall(475,290,10,70))
walls.append(Wall(410,290,135,10))
walls.append(Wall(410,215,10,80))
walls.append(Wall(535,140,10,150))
walls.append(Wall(350,215,70,10))
walls.append(Wall(350,140,10,80))
walls.append(Wall(290,140,70,10))
walls.append(Wall(475,140,135,10))
walls.append(Wall(475,140,10,75))
walls.append(Wall(545,360,135,10))
walls.append(Wall(600,215,130,10))
walls.append(Wall(600,215,10,75))


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
    niger.move()
    peri.draw(window)
    niger.draw(window)
    pygame.display.flip()
    fps.tick(60)