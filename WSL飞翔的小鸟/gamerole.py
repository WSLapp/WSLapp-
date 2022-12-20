# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Created on Thu Dec 25  2016
@author: LINJUNJI  
@mail: ljj6@mail2.sysu.edu.cn 
"""


import pygame
import random

SCREEN_WIDTH =384
SCREEN_HEIGHT=448
INTERVEL=120         #两个障碍之间的间隔
UP_LIMIT=60
DOWN_LIMIT=360

#小鸟类
class Bird(pygame.sprite.Sprite):
    def __init__(self,bird_imgs,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=bird_imgs
        self.rect=self.image[0].get_rect()
        self.rect.midbottom=init_pos
        self.up_speed = 7
        self.down_speed=4
        self.selfdown_speed=2
        self.image_index=0          #图片索引参数，控制小鸟飞行姿态变化
        self.is_hit=False 
        self.is_downtoground=False
    
    def SelfMoveDown(self):
        self.rect.top += self.selfdown_speed
    
    def SelfDiedDown(self):
        self.up_speed = 0
        self.down_speed=0
        self.rect.bottom +=self.selfdown_speed*2
        if self.rect.bottom >=400:
            self.rect.bottom =400
            self.is_downtoground=True
        
    def moveUp(self):
        if self.rect.top<=0:
            self.rect.top=0
        else:
            self.rect.top -=self.up_speed
            
    def moveDown(self):
        if self.rect.top>=SCREEN_HEIGHT-self.rect.height:
            self.rect.top = SCREEN_HEIGHT-self.rect.height
        else:
            self.rect.top += self.down_speed
    '''        
    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed
    '''
#柱子类
class Pilar(pygame.sprite.Sprite):
    def __init__(self,pilar_image_up,pilar_image_down,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.pilar1_image=pilar_image_up
        self.pilar2_image=pilar_image_down
        self.pilar1_rect=self.pilar1_image.get_rect()
        self.pilar2_rect=self.pilar2_image.get_rect()
        self.pilar1_rect.bottomleft=init_pos
        self.pilar2_rect.topleft=[init_pos[0],init_pos[1]+INTERVEL]
        self.horizontal_speed=2  #柱子平移的速度
        #self.vertical_speed=0.3    #柱子上下移动的速度
        #self.direction=random.randint(0,1)  #柱子上下移动的方向
        
    def move(self):
        self.pilar1_rect.left -=self.horizontal_speed   #柱子左右移动
        self.pilar2_rect.left -=self.horizontal_speed
        #if self.direction == 1:                           #控制柱子上下移动
        #    self.pilar1_rect.bottom +=self.vertical_speed        
        #    self.pilar2_rect.top +=self.vertical_speed
        #    if self.pilar2_rect.top > DOWN_LIMIT:
        #        self.direction=0
        #else:
        #    self.pilar1_rect.bottom -=self.vertical_speed        
        #    self.pilar2_rect.top -=self.vertical_speed
        #    if self.pilar1_rect.bottom < UP_LIMIT:
        #        self.direction=1
    def stop(self):
        self.horizontal_speed=0
        self.vertical_speed=0
