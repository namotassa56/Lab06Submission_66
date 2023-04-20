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
btn = Button(350,240,100,40) # สร้าง Object จากคลาส Button ขึ้นมา


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.save = self.text
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(100, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
    def showsave(self):
        return self.save

class age:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.save = self.text
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(100, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
    def showsave(self):
        return self.save


run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
rec = Rectangle(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา


font = pg.font.Font('freesansbold.ttf', 20) # font and fontsize
# text = font.render('FRA 142', True, (0,0,102), (255,255,255)) # (text,is smooth?,letter color,background color)
# textRect = text.get_rect() # text size
# textRect.center = (win_x // 2, win_y // 2)
text = font.render('FIRST NAME', True, (0,0,102), (255,255,255))
text1 = font.render('LAST NAME', True, (0,0,102), (255,255,255))
text2 = font.render('AGE', True, (0,0,102), (255,255,255))
text3 = font.render('SUBMIT', True, (0,0,0))



COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(90, 100, 100, 32) # สร้าง InputBox1
input_box2 = InputBox(350, 100, 100, 32) # สร้าง InputBox2
input_box3 = InputBox(616, 100, 100, 32)
input_boxes = [input_box1, input_box2,input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True
switch = 0



while run:
    screen.fill((255, 255, 255))
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        screen.blit(text, (90, 68))
        screen.blit(text1, (350, 68))
        screen.blit(text2, (616, 68))
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    if btn.isMouseOn():
        btn.r = 0
        btn.g = 204
        btn.b = 0
        if pg.mouse.get_pressed()==(1,0,0):
            btn.r = 25
            btn.g = 51
            btn.b = 0
            switch = 1
        
    else:
        btn.r = 51
        btn.g = 255
        btn.b = 51
    btn.draw(screen)
    if switch == 1:
        submit = font.render('hello '+str(input_box1.text)+' '+str(input_box2.text)+'! You are '+str(input_box3.text)+' years old.',True,(0,0,0))
        screen.blit(submit, (250, 400))

    screen.blit(text3, (363,250))

    pg.time.delay(1)
    pg.display.update()