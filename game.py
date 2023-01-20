import pygame

screen=pygame.display.set_mode(size=(500,500))
screen.fill((240,248,255))
pygame.display.flip()
running=True
while running :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False


