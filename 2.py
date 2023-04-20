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

run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
rec = Rectangle(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    rec.draw(screen)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            rec.x +=1
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            rec.x -=1
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #W
            rec.y -=1
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            rec.y +=1

