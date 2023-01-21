import pygame
import random
pygame.init()
size_x=500
size_y=500
screen=pygame.display.set_mode(size=(size_x,size_y))
pygame.display.set_caption('Snake Game')
screen.fill((180,180,180))
pygame.display.flip()
def message(msg,center,size):
    font = pygame.font.SysFont('times new roman',size)
    text = font.render(msg, True, (0,0,0),None)
    textRect = text.get_rect()
    textRect.center = center
    screen.blit(text,textRect)
    
def game_over():
    message('Over!',(250,250),40)
    pygame.display.flip()

    
snake_x=120
snake_y=220
snake_body=[[120,220],[110,220],[100,250],[90,250]]
fruit_x=random.randint(30,47)*10
fruit_y=random.randint(30,47)*10
fruit=[fruit_x,fruit_y,10,10]
fruit_run=True
score=0

fps=pygame.time.Clock()  
   
x_change=0
y_change=0
running=True

while running :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    if event.type== pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            y_change = -10
            x_change = 0
        if event.key == pygame.K_DOWN:
            y_change = 10
            x_change = 0
        if event.key == pygame.K_LEFT:
            x_change = -10
            y_change = 0
        if event.key == pygame.K_RIGHT:
            x_change = 10
            y_change = 0
    
        
    snake_x +=x_change
    snake_y +=y_change
    
    

    snake_body.insert(0,[snake_x,snake_y])
    if snake_x==fruit_x and snake_y==fruit_y:
        fruit_run=False
        score +=1
        print(score)
    else:
        snake_body.pop()

    if  fruit_run==False:
        fruit_x=random.randint(30,47)*10
        fruit_y=random.randint(30,47)*10
        fruit=[fruit_x,fruit_y,10,10]
    fruit_run=True

    screen.fill((240,248,255))
    pygame.draw.rect(screen,(197,197,197),[30,30,450,450])
    for body in snake_body:
        pygame.draw.rect(screen,(0,0,0),[body[0],body[1],10,10])
    pygame.draw.rect(screen,(255,0,0),fruit)
    message('Score:'+str(score),(60,10),20)
    pygame.display.update()

    if snake_x<=20 or snake_x>=480 or snake_y<=20 or snake_y>=480:
        message('Score:'+str(score),(250,200),40)
        message('Over!',(250,250),40)
        pygame.display.flip()
        #game_over()
   
    #score_show()
    fps.tick(20)
    pygame.display.update()

pygame.display.update()

