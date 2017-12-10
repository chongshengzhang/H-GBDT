
import cv2
import numpy as np
import skimage.feature
import SWH_H

def LEP_HOG(image_jar):
    hist, images = SWH_H.SWHH(image_jar)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    features = []
    for image in images:
        imgSize = image.shape;
        region_x = [1, 1, 0,-1,-1,-1, 0, 1]
        region_y = [0,-1,-1,-1, 0, 1, 1, 1]
        LEPFeat = np.zeros([imgSize[0] - 2, imgSize[1] - 2], np.int)
        for i in range(1, imgSize[0]-1):
            for j in range(1, imgSize[1]-1):
                # print(image[i,j])
                p = []
                center = image[i, j]
                for k in range(0, len(region_x)):
                    p.append(image[i + region_x[k], j + region_y[k]] - center)

                I = np.zeros([len(p) / 2], np.int)
                for k in range(0,len(I)):
                    if (p[k] * p[k + 4]) > 0:
                        I[k] = 2**k
                LEPFeat[i-1,j-1] = sum(I)

        feature = skimage.feature.hog(LEPFeat,
                                      pixels_per_cell=(12, 12),
                                      cells_per_block=(2, 2)
                                      )
        features.append(feature)
    return features





# img = cv2.imread('1.jpg')
# HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# H,S,V = cv2.split(HSV)
# LBP = LEP_HOG(V)
# print(LBP, len(LBP))
#
# print(LBP)
# feature = skimage.feature.hog(LBP,
#                               pixels_per_cell=(12, 12),
#                               cells_per_block=(2, 2)
#                               )
# print(feature, len(feature))














