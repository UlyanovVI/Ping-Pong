import pygame
from time import *
pygame.init()
w = pygame.display.set_mode((700,700))
w.fill((255,255,255))
pygame.display.update()
clock = pygame.time.Clock()
clock.tick(40)
back = (255,255,255)

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
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

ball = Picture('shar.png',250,240,70,70,None)
pl1 = Picture('platforma.png',225,600,200,70,None)
pl2 = Picture('platforma1.png',225,100,200,70,None)
move_r = False
move_l = False
move_r1 = False
move_l1 = False
speed_xb = 3
speed_yb = 3
speed_xpl = 3
speed_ypl = 3
go = False
choose = False

while not go:
    ball.fill1(back)
    pl1.fill1(back)
    pl2.fill1(back)

    if not choose:
        
        modLfon = Area(0,0,350,700,(0,255,0))
        modLfon.set_text(' ',35,(0,0,0))
        modLfon.draw1(0,0)
        modLfon.fill1((0,255,0))
        modHfon = Area(350,0,350,700,(0,255,0))
        modHfon.set_text(' ',35,(0,0,0))
        modHfon.draw1(0,0)
        modHfon.fill1((255,0,0))

        modH = Area(375,390,10,10,(0,0,0))
        modH.set_text('>Hard',35,(0,0,0))
        modH.draw1(270,390)
        modL = Area(235,390,10,10,back)
        modL.set_text('Lite<',35,(0,0,0))
        modL.draw1(270,10)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    choose = True
                    speed_xb = 5
                    speed_yb = 5
                    speed_xpl = 5
                    speed_ypl = 5
                    w.fill((255,255,255))
                if event.key == pygame.K_LEFT:
                    choose = True
                    speed_xb = 3
                    speed_yb = 3
                    speed_xpl = 3
                    speed_ypl = 3
                    w.fill((255,255,255))
    else:
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

        if move_r:
            pl1.rect.x += speed_xpl
        if move_l:
            pl1.rect.x -= speed_xpl
        if move_r1:
            pl2.rect.x -= speed_xpl
        if move_l1:
            pl2.rect.x += speed_xpl
    
        ball.rect.x -= speed_xb
        ball.rect.y -= speed_yb
        if ball.colliderect(pl1.rect):
            speed_yb *= -1
        if ball.colliderect(pl2.rect):
            speed_yb *= -1
        if ball.rect.y < 0:
            speed_yb *= -1
        if ball.rect.x > 600 or ball.rect.x < 0:
            speed_xb *= -1
        if ball.rect.y > (pl1.rect.y + 50) or ball.rect.y < (pl2.rect.y - 50):
            lose = Area(270,350,50,50,back)
            lose.set_text('LOSE!!!',35,(255,0,0))
            lose.draw1(10,10)
            go = True
    if event.type == pygame.QUIT:
        go = True

    pl1.draw()
    pl2.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(60)