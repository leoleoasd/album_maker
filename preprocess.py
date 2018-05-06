#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from PIL import Image
j=0
for i in os.listdir("./data"):
    print(i)
    '''
    os.system("mv \"./data/{}\" ./data/{}.jpg".format(i,j))
    j=j+1
    continue
    '''
    image = Image.open("./data/{}".format(i))
    image.resize((1920,1080),Image.ANTIALIAS)
    black = Image.new("RGB",(1920,1080))
    siz = image.size;
    if(siz[0] / siz[1] > 16/9):
        black.paste(
            image.resize(
                (1920,int(1920*(siz[1]/siz[0])))
            ),
            (
                0,int((1080-int(1920*(siz[1]/siz[0])))/2)
            )
        )
    else:
        # 比16:9 瘦的图
        black.paste(
            image.resize(
                (int(1080*(siz[0]/siz[1])),1080) # 缩放到高为1080p 宽不影响长宽比
            ),
            (
                int(
                    (1920-(int(1080*(siz[0]/siz[1]) # 1920-之前的宽在初以二 居中
                    ),1080)[0])/2),
                0
            )
        )

    black.save("./images/{}.jpg".format(i),"jpeg")
    j+=1
