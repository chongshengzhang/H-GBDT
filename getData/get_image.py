import os
import skimage.io
from skimage import transform
from util import reflect_get_class
from FMCF import SWH_H, LEPHOG, LDO_V
import  numpy as np
import cv2

def getImage(lines, BASE_DIR):
    image_jar = dict()
    image_jar['rgb'] = list()
    image_jar['gray'] = list()
    data = []
    scales = []
    imgSize = 125;
    for line in lines:
        imageInfo = line.strip().split(" ");
        image_name = os.path.join(BASE_DIR, imageInfo[0])
        # print (imageInfo[0])
        image = cv2.imread(image_name)
        x = int(imageInfo[1])
        y = int(imageInfo[2])
        width = int(imageInfo[3])
        height = int(imageInfo[4])
        # print (image)
        # roi = image[y:y + width, x:x + height]
        try:
            roi = image[y:y + width, x:x + height, :]
        except:
            roi=roi
        # print(roi.shape)
        image_jar['rgb'].append(cv2.resize(roi, (imgSize, imgSize)))
        # print (cv2.resize(roi, (imgSize, imgSize))[:, :, 0])
        # tr = transform.resize(roi, (125, 125))
        # print(tr.shape)
        # HSV = cv2.cvtColor(tr, cv2.COLOR_BGR2HSV)
        # print(HSV)

        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        dst = cv2.equalizeHist(gray)
        dst = transform.resize(dst, (imgSize, imgSize))
        #
        scale = width / float(imgSize)
        # print (scale)
        str = line.strip().split(' ')[7::]
        # print(str)
        temp = []
        for s in str:
            temp.append(float(s) / scale)
        data.append(temp)
        scales.append(scale)
        image_jar['gray'].append(skimage.img_as_ubyte(dst))
    return image_jar,data,scales

def getMixData(feature, part_data, index):
    x = [];
    y = [];
    i = 0;
    for k in range(0,len(feature)):
        if k>=len(part_data):
            i = k%len(part_data)
            # print (k, i,len(x[i]), len(feature[k]), type(x[i]), type(feature[k]))
            if k>= 2*len(part_data):
                temp = x[i].tolist() + feature[k].tolist()
            else:
                # print ('xvccbv');
                temp = x[i] + feature[k].tolist()
            x[i] = np.array(temp)
            # print (len(x[i]),type(x[i]),type(feature[k]), len(x),len(feature))
        else:
            x.append(feature[k].tolist())
            y.append(part_data[k][index])
    return x, y



def getFeature(config, image_jar):
    feature_jar = dict()
    for feature_name in [x.strip() for x in config['general']['UseFeature'].strip().split(',')]:
        conf_item_name = 'features.{}'.format(feature_name).lower()
        if feature_name == 'swhh':
            feature_jar[conf_item_name] = SWH_H.SWHH(image_jar)[0]
            # print (len(feature_jar[conf_item_name] ), len(image_jar), 'zjdskduhsidu')
        elif feature_name == 'lephog':
            feature_jar[conf_item_name] = LEPHOG.LEP_HOG(image_jar)
        elif feature_name == 'ldohog':
            feature_jar[conf_item_name] = LDO_V.LDOV(image_jar)
        elif '_' in feature_name:
            conf = format(feature_name).lower()
            # feature_name  = "features." + feature_name
            feature_name = 'features.{}'.format(feature_name).lower()
            feature_jar[conf_item_name] = [];
            # print(conf)
            # features = []
            for conf_name in conf.split('_'):
                # print(conf_name)
                feature_conf = config['features.{}'.format(conf_name).lower()]
                # print (feature_conf)
                feature_class_name = "features.feature_{}.Feature{}".format(conf_name, conf_name.capitalize())
                # print(feature_class_name)
                feature_class_obj = reflect_get_class(feature_class_name)(feature_conf)
                feature_jar[feature_name] = feature_jar[feature_name] + feature_class_obj.extract_all(image_jar)

            print (len(feature_jar[feature_name]))
            features = []
            for k in xrange(len(feature_jar[feature_name])):
                num = len(image_jar['rgb'])
                # print (num)
                if k >= num:
                    # print
                    i = k%num
                    # print (len(features[i]), type(features[i]), type(feature_jar[feature_name][k]))
                    if k >= 2*num:
                        temp = features[i] + feature_jar[feature_name][k].tolist()
                    else:
                        temp = features[i].tolist() + feature_jar[feature_name][k].tolist()

                    # features[i] = np.array(temp)
                    features[i] = temp
                else:
                    features.append(feature_jar[feature_name][k])
            feature_jar[feature_name] = features
            print (len(features[0]))
        else:
            print(feature_name)
            # conf_item_name = 'features.{}'.format(feature_name).lower()
            feature_conf = config[conf_item_name]
            # Get the class and build the instance with the configuration file
            feature_class_name = "features.feature_{}.Feature{}".format(feature_name, feature_name.capitalize())
            # print (feature_class_name)
            feature_class_obj = reflect_get_class(feature_class_name)(feature_conf)
            feature_jar[conf_item_name] = feature_class_obj.extract_all(image_jar)
    return feature_jar

def getMixData(feature, part_data, index):
    x = [];
    y = [];
    i = 0;
    for k in range(0,len(feature)):
        if k>=len(part_data):
            i = k%len(part_data)
            # print (k, i,len(x[i]), len(feature[k]), type(x[i]), type(feature[k]))
            if k>= 2*len(part_data):
                temp = x[i].tolist() + feature[k].tolist()
            else:
                # print ('xvccbv');
                temp = x[i] + feature[k].tolist()
            x[i] = np.array(temp)
            # print (len(x[i]),type(x[i]),type(feature[k]), len(x),len(feature))
        else:
            x.append(feature[k].tolist())
            y.append(part_data[k][index])
    return x, y



#
# def geMextFeature(config, image_jar):
#     feature_jar = dict()
#     for feature_name in [x.strip() for x in config['general']['UseFeature'].split(',')]:
#         # Get the configuration
#         conf_item_name = 'features.{}'.format(feature_name).lower()
#
#         print (conf_item_name)
#         conf = format(feature_name).lower()
#         feature_jar[feature_name]=[];
#         print(conf)
#         for conf_name in conf.split('_'):
#             conf_item_name = 'features.{}'.format(feature_name).lower()
#             if feature_name == 'swhh':
#                 feature_jar[conf_item_name] = SWH_H.SWHH(image_jar)
#             elif feature_name == 'lephog':
#                 feature_jar[conf_item_name] = LEPHOG.LEP_HOG(image_jar)
#             elif feature_name == 'ldohog':
#                 feature_jar[conf_item_name] = LDO_V.LDOV(image_jar)
#             else:
#                 print(feature_name)
#                 # conf_item_name = 'features.{}'.format(feature_name).lower()
#                 feature_conf = config[conf_item_name]
#                 # Get the class and build the instance with the configuration file
#                 feature_class_name = "features.feature_{}.Feature{}".format(feature_name, feature_name.capitalize())
#                 # print (feature_class_name)
#                 feature_class_obj = reflect_get_class(feature_class_name)(feature_conf)
#                 feature_jar[conf_item_name] = feature_class_obj.extract_all(image_jar)
#
#     return feature_jar

