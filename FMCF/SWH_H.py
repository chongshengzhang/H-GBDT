# -*- coding utf-8 -*-
# coding=utf-8
'''
S-weight histogram of H-channel(SWH-H)
In the HSV color space, hue component corresponds to the color infomation and the value of hue is defined as angle, varying from from 0-360 ,
# extract the histogram of color information from H-channel and apply the value of saturation as the weight of hue's value instead of equality.
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
import RGB2HSV

def SWHH(image_jar):
    images = image_jar['rgb']
    # SSS = cv2.cvtColor(images[0], cv2.COLOR_BGR2HSV)
    hist= []
    VChannel = []
    for image in images:
        # print (image)
        B, G, R = cv2.split(image)
        imgSize = image.shape
        # print(imgSize)
        H = np.zeros([imgSize[0], imgSize[1]], np.float32)
        S = np.zeros([imgSize[0], imgSize[1]], np.float32)
        V = np.zeros([imgSize[0], imgSize[1]], np.float32)

        hnum =  np.zeros([360], np.float32)
        for i in range(0, imgSize[0]):
            for j in range(0, imgSize[1]):
                # print (R[i,j], G[i,j], B[i,j])
                H[i,j], S[i,j],V[i,j] = RGB2HSV.rgb2hsv(R[i,j], G[i,j], B[i,j])
                hnum[H[i,j]-1] = hnum[H[i,j]-1] + S[i,j]

        hist.append(hnum)
        VChannel.append(V)
    # print (len(hist), 'hist')
    return hist, VChannel





