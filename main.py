import pygame
import sys
from setting import *
from event import EVENT

pygame.init()
run = True

background = pygame.image.load(r'C:\Users\a\Desktop\제비\asset\base.png')

class button(pygame.sprite.Sprite):
    def __init__ (self,numb,x,y):
        super().__init__()
        self.numb = numb
        self.animate_1 = numb
        self.animate_2 = numb + 1
        self.x = x
        self.y = y
        self.asset = [
            pygame.image.load(r'C:\Users\a\Desktop\제비\asset\자동등록.png'),
            pygame.image.load(r'C:\Users\a\Desktop\제비\asset\자동등록_1.png')
        ]
        self.image = self.asset[self.numb]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    def get_input(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_clicked = pygame.mouse.get_pressed()[0]
        if (self.x + self.rect.width > self.mouse_pos[0] > self.x) and (self.y + self.rect.height > self.mouse_pos[1] > self.y):
            self.numb = self.animate_2
            if self.mouse_clicked:
                print('1')
        else:
            self.numb = self.animate_1  
              

    def animate(self):
        self.image = self.asset[self.numb]

    
    def update(self):
        self.get_input()
        self.animate()



button_group = pygame.sprite.Group(button(0,90,225))

screen = pygame.display.set_mode((w,h))

while run:
    screen.blit(background,(0,0))
    button_group.draw(screen)
    button_group.update()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

sys.exit()