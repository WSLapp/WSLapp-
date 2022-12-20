# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Created on  Dec 25 2016
@author: LINJUNJI  
@mail: ljj6@mail2.sysu.edu.cn 
"""
import pygame
from sys import exit
import random
from pygame.locals import *
from pygame.font import *  
from gamerole import *
import os
import datetime
import numpy as np
import operator

#图片路径信息
BackGround_image_path1='./sources/background/day.png'          #背景图片
BackGround_image_path2='./sources/background/night.png'

GetStart_image_path='./sources/guide/day/down.png'           #开始界面
GameOver_image_path='./sources/other/gameover.png'
Restart_image_path='./sources/other/restart.png'

Grade_blackball_path='./sources/other/grade_blackball.png'
white_gold_Medal_image_path='./sources/medal/white_gold_medal.png'  #奖牌图片
gold_image_path='./sources/medal/gold_medal.png'
silver_medal_image_path='./sources/medal/silver_medal.png'
bronze_medal_image_path='./sources/medal/bronze_medal.png'

Ground_image_path='./sources/background/ground.png'         #地面图片

pilar_image_up_path='./sources/pilar/up.png'                #柱子图片
pilar_image_down_path='./sources/pilar/down.png'
Bird_image1_path='./sources/bird/up.png'                   #小鸟图片
Bird_image2_path='./sources/bird/med.png'
Bird_image3_path='./sources/bird/down.png'

#游戏窗体设置
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('WSL飞翔的小鸟') 

#图片载入      
background_day=pygame.image.load(BackGround_image_path1)
background_night=pygame.image.load(BackGround_image_path2)
ground=pygame.image.load(Ground_image_path)
pilar_image_up=pygame.image.load(pilar_image_up_path)
pilar_image_down=pygame.image.load(pilar_image_down_path)
get_start_image=pygame.image.load(GetStart_image_path)
gameover_image=pygame.image.load(GameOver_image_path)
medal_blackball_image=pygame.image.load(Grade_blackball_path)
restart_image=pygame.image.load(Restart_image_path)

bird_images=[]
bird_image_up=pygame.image.load(Bird_image1_path)
bird_image_med=pygame.image.load(Bird_image2_path)
bird_image_down=pygame.image.load(Bird_image3_path)
bird_images.append(bird_image_up)
bird_images.append(bird_image_med)
bird_images.append(bird_image_down)

medal_images=[]
medal1=pygame.image.load(white_gold_Medal_image_path)
medal2=pygame.image.load(gold_image_path)
medal3=pygame.image.load(silver_medal_image_path)
medal4=pygame.image.load(bronze_medal_image_path)
medal_images.append(medal1)
medal_images.append(medal2)
medal_images.append(medal3)
medal_images.append(medal4)

#新建小鸟
bird_pos=[190,190]  #小鸟初始位置
mybird=Bird(bird_images,bird_pos)

#柱子集合
pilar_set = pygame.sprite.Group()

#运行参数设置
pilar_frequency=0  #柱子更新参数
bird_frequency=0   #小鸟飞行频率
clock = pygame.time.Clock()
running=False
score=0
flag=1

def collide_circle(pilar, mybird):  #碰撞检测函数
    if mybird.rect.right > pilar.pilar1_rect.left and mybird.rect.left < pilar.pilar1_rect.right:
        if (mybird.rect.top >pilar.pilar1_rect.bottom and mybird.rect.bottom <pilar.pilar2_rect.top):
            return False
        else:
            return True
    else:
        if mybird.rect.bottom > 400:
            return True
        else:
            return False
    
def get_history_record(score):     #获取记录的得分
    record=[]
    index =0
    if os.path.isfile("record.txt"):      #存在：获取记录到的内容  
        f=open("record.txt")
        line=f.readline()
        line=f.readline()
        while line !="":
            record.append([int(line.strip().split(",")[0]),line.strip().split(",")[1]])
            line=f.readline()
        f.close()
    record.append([score,str(datetime.datetime.now())])
    record.sort(key=operator.itemgetter(0),reverse=True)
    #print(record)
    while len(record)>10:
        record.pop()
    file_writer = open("record.txt", 'w')
    file_writer.writelines("time"+","+"grade"+"\n")
    for i in range(len(record)):
        file_writer.writelines(str(record[i][0])+","+str(record[i][1])+"\n")
        if int(record[i][0]) == int(score):
            index=i
    file_writer.close()
    if index >3:
        index=3
    return record[0][0],index
    
    
while not running:
    clock.tick(60)   
    screen.fill(0)
    screen.blit(get_start_image, (0, 0)) 
    pygame.display.update()
    x, y=pygame.mouse.get_pos()   
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if y<380 and y>300 and x>180 and x <210:
                running=True
    
while True:
    clock.tick(60)   
    pilar_frequency +=1    
    #生成柱子
    if pilar_frequency %100==0:
        aaa=385
        #global aaa
        pilar_pos=[384,random.randint(130, 250)]
        new_pilar=Pilar(pilar_image_up, pilar_image_down, pilar_pos)
        pilar_set.add(new_pilar)
        aaa-=1
    #global aaa
    if pilar_frequency >=1000:
        pilar_frequency=0 
        flag=(-1)*flag       
    #移动柱子
    for pilar in pilar_set:
        pilar.move()
        if collide_circle(pilar, mybird):  #碰撞检测代码
            mybird.is_hit=True 
            for pilar in pilar_set:
                pilar.stop()
        if pilar.pilar1_rect.right <0:
            pilar_set.remove(pilar) 
    #小鸟降落
    mybird.SelfMoveDown() 
    # 绘制背景
    screen.fill(0)
        
    if flag==1:
        screen.blit(background_day, (0, 0)) 
    else:
        screen.blit(background_night, (0, 0))
    #绘制柱子
    for pilar in pilar_set:
        screen.blit(pilar.pilar1_image,pilar.pilar1_rect)
        screen.blit(pilar.pilar2_image,pilar.pilar2_rect)
    #绘制地面   
    screen.blit(ground,(0,384))
    #绘制玩家小鸟
    bird_frequency +=1   
    if not mybird.is_hit:  #未发生碰撞
        score +=1
        screen.blit(mybird.image[mybird.image_index],mybird.rect)
        mybird.image_index=bird_frequency % 3
    else:  #发生碰撞
        running=False 
        mybird.SelfDiedDown()
        screen.blit(mybird.image[0],mybird.rect)
        has_log=False
        while not running and mybird.is_downtoground:     #画面切换到结束界面           
            screen.blit(gameover_image,(64,30))
            screen.blit(medal_blackball_image,(42,100))
            screen.blit(restart_image,(122,270))
            if not has_log:                   
                bestscore,index=get_history_record(score/100) #获取历史记录情况
                #print(score/100)
                #print(bestscore,index)
                has_log=True
            screen.blit(medal_images[index],(75,160))        #要读取之前保存的信息，
            x, y=pygame.mouse.get_pos()  
            
            #目前得分
            score_font = pygame.font.Font(None, 36)
            score_text = score_font.render(str(score//100), True, (255,255,255))
            text_rect = score_text.get_rect()
            text_rect.midtop = [290, 145]
            screen.blit(score_text, text_rect)
            #历史最佳得分
            score_font = pygame.font.Font(None, 36)
            score_text = score_font.render(str(bestscore), True, (255,255,255))
            text_rect = score_text.get_rect()
            text_rect.midtop = [290,200]
            screen.blit(score_text, text_rect)
            
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if y<360 and y>280 and x>150 and x <240:  #重新开始
                        pilar_set = pygame.sprite.Group()
                        mybird=Bird(bird_images,bird_pos)
                        score=0
                        running=True
            pygame.display.update()            
        
    # 绘制得分  
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(score//100), True, (255,255,255))
    text_rect = score_text.get_rect()
    text_rect.midtop = [185, 30]
    screen.blit(score_text, text_rect)

    #屏幕更新
    pygame.display.update()
    #绘制按键执行代码
    key_pressed=pygame.key.get_pressed()
    if not mybird.is_hit:
        if key_pressed[K_SPACE] or key_pressed[K_UP]:
            mybird.moveUp()
        if key_pressed[K_LSHIFT] or key_pressed[K_DOWN]:
            mybird.moveDown()
        
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
            
    

