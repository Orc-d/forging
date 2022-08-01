import pygame

class spritesheet():
    def __init__(self,filename):
        
        self.sheet = pygame.image.load(filename)
        
    def load_image(self,numb,w=200,h=200):
        self.x = (numb - 1) % 5 * w
        self.y = (numb - 1) // 5 * h
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.image = pygame.Surface(self.rect.size)
        self.image.blit(self.sheet,(0,0),self.rect)
        return self.image
        