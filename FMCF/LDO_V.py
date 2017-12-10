
from FMCF.SWH_H import SWHH
import skimage.feature

def yLDOV(image_jar):
    hist, images = SWHH(image_jar)
    # print (images[0])
    features = []
    for image in images:
        # print('ddd')
        # print (image)
        feature = skimage.feature.hog(image,
                                      pixels_per_cell=(12, 12),
                                      cells_per_block=(2, 2)
                                      )
        features.append(feature)
        # print(feature)
    return features






