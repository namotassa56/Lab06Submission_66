import sys 
import pygame as pg
pg.init()


class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,r=0,g=0,b=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.r = r
        self.g = g
        self.b = b
    def draw(self,screen):
        pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    
    def isMouseOn(self):
        mouseX , mouseY=pg.mouse.get_pos()
        if mouseX >= self.x and mouseX <= self.x+self.w and mouseY >= self.y and mouseY <= self.y + self.h:
            return True
        else:
            return False
    # def isMouseOff(self):
    #     mouseX , mouseY=pg.mouse.get_pressed()
    #     if mouseX == 0 and mouseY == 0:
    #         return True
    #     else:
    #         return False


run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        btn.r = 220
        btn.g = 220
        btn.b = 220
        if pg.mouse.get_pressed()==(1,0,0):
            btn.r = 120
            btn.g = 20
            btn.b = 220
    else:
        btn.r = 250
        btn.g = 0
        btn.b = 0
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False