import pygame
from time import *
pygame.init()
w = pygame.display.set_mode((700,700))
w.fill((255,255,255))
pygame.display.update()
clock = pygame.time.Clock()
clock.tick(40)
back = (255,255,255)

class Area:
    def __init__(self,x=0,y=0,width=10,height=10,color=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = color
    def colliderect(self,rect):
        return self.rect.colliderect(rect)
    def fill1(self,back):
        pygame.draw.rect(w,back,self.rect)
    def draw1(self,x,y):
        w.blit(self.image,(self.rect.x,self.rect.y))
    def set_text(self,text,fsize=12,text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana',fsize).render(text,True,text_color)
class Picture(Area):
    def __init__(self,filename=None,x=0,y=0,width=10,height=10,color=None):
        Area.__init__(self,x=x,y=y,width=width,height=height,color=None)
        self.image = pygame.image.load(filename)
    def draw(self):
        w.blit(self.image,(self.rect.x,self.rect.y))

ball = Picture('shar.png',250,240,60,60,None)
pl1 = Picture('platforma.png',225,600,200,70,None)
pl2 = Picture('platforma1.png',225,100,200,70,None)
move_r = False
move_l = False
move_r1 = False
move_l1 = False
speed_x = 3
speed_y = 3
go = False
while not go:
    ball.fill1(back)
    pl1.fill1(back)
    pl2.fill1(back)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_r = True
            if event.key == pygame.K_LEFT:
                move_l = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_r = False
            if event.key == pygame.K_LEFT:
                move_l = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_r1 = True
            if event.key == pygame.K_a:
                move_l1 = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_r1 = False
            if event.key == pygame.K_a:
                move_l1 = False
        if event.type == pygame.QUIT:
            go = True

    if move_r:
        pl1.rect.x += 3
    if move_l:
        pl1.rect.x -= 3
    if move_r1:
        pl2.rect.x -= 3
    if move_l1:
        pl2.rect.x += 3
    pl1.draw()
    pl2.draw()
    
    ball.rect.x -= speed_x
    ball.rect.y -= speed_y
    if ball.colliderect(pl1.rect):
        speed_y *= -1
    if ball.colliderect(pl2.rect):
        speed_y *= -1
    if ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x > 600 or ball.rect.x < 0:
        speed_x *= -1
    if ball.rect.y > (pl1.rect.y + 50) or ball.rect.y < (pl2.rect.y - 50):
        lose = Area(270,350,50,50,back)
        lose.set_text('LOSE!!!',35,(255,0,0))
        lose.draw1(10,10)
        go = True

    ball.draw()
    pygame.display.update()
    clock.tick(40)