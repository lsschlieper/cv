# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 09:39:19 2022

@author: luciano.schlieper
"""
import os
from os import listdir
from os.path import isfile, join

import sys
import pygame
from pygame.locals import *


mypath = 'C:\\Users\\luciano.schlieper\\Downloads\\cv-main\\data\\maps'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

bw, bh = 350, 280
ratio = 1.25


pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)


for k in range(len(onlyfiles)):
    imgPath = mypath + '\\' + onlyfiles[k]
    print(imgPath)

    imgSurf = pygame.image.load(imgPath)
    x, y, w, h = imgSurf.get_rect()
    
    imgRatio = w/h
    t=0
    if imgRatio < ratio:
        t = 1
    print(w, h)
    print(imgRatio, t)
    if t == 0:
        nw = w
        nh = w*0.8
        
        mw = 0
        mh = (nh-h)/2
        
        print('nw', nw, 'nh', nh)
        print('mw', mw, 'my', mh)
        
    if t == 1:

        nw = h*1.25
        nh = h
        
        mw = (nw-w)/2
        mh = 0
        
        print('nw', nw, 'nh', nh)
        print('mw', mw, 'my', mh) 


    myNewSurface = pygame.Surface((nw, nh))
    myNewSurface.fill((255,255,255))

    # myNewSurface = Surface((nw, nh))
    myNewSurface.blit(imgSurf, (mw, mh))
    
    
    iMiniFilepath = mypath + '\\mini\\' + onlyfiles[k]
    
    surfTosave = pygame.Surface((bw*2,bh*2))
    
    pygame.transform.scale(myNewSurface, (bw*2, bh*2), surfTosave)
    
    # print(surfTosave.get_rect())
    
    pygame.image.save(surfTosave, iMiniFilepath)
    
    print('=======')
    # if w > h:
    #     t = 0
    # else:
    #     t = 1
           
    # print(w, h, t)

    # if t == 0:
    #     wr = w/bw
    
    # print(wr)

 




 

# set up the window










sys.exit()


mypath = 'C:\\Users\\luciano.schlieper\\Downloads\\cv-main\\data\\maps'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for k in range(len(onlyfiles)):
       
    iNewName = str(k+1) + '.jpg' 
    iNewFilepath = mypath + '\\new\\' + iNewName
    iOldFilePath = mypath + '\\' + onlyfiles[k]
    
    print(iOldFilePath)
    print(iNewFilepath)
    print('-')
    os.popen('copy ' + iOldFilePath + ' ' + iNewFilepath)

# print(onlyfiles)