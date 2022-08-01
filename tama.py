import pygame
import numpy as np
from spritesheet import spritesheet

pygame.init()

class digitama(pygame.sprite.Sprite):
    def __init__(self,numb):
        super().__init__()
        
        self.image = spritesheet(r'C:\Users\a\Desktop\제비\asset\Digitama_Image\DIGITAMA.png')
        self.image = self.image.load_image(numb,200,200)
        self.image = pygame.transform.scale(self.image,(55,55))
        self.x_pos = 18
        self.y_pos = 233
        
        self.rect = pygame.Rect(self.x_pos,self.y_pos,200,200)
    
    def random_selection(self):
        self.rand = int(np.random.randint(1,38))
        
        return self.rand