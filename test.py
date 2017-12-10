# # -*- coding: UTF-8 -*-
import os
from sklearn.ensemble import GradientBoostingRegressor
import configparser
from numpy import *
from getData import load_data, get_image
from decimal import Decimal
import pickle
from PIL import Image
import ImageDraw

# Constant
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIR_PICTURE = os.path.join(BASE_DIR, 'images')
DIR_MODEL = os.path.join(BASE_DIR, 'models')
# Read the configure file
config = configparser.ConfigParser()
config.read('config.ini')
# read infomation of images
f = open(config['general']['path'],"r")
lines = f.readlines()
f.close();
print('get image_jar, part_data')
image_jar, part_data, Tscales = get_image.getImage(lines, BASE_DIR)

feature_jar = get_image.getFeature(config, image_jar)

#  predict point
# read testing images
f = open(config['general']['testSet'],"r")
predict = f.readlines()
f.close()

# print('testImage_jar, predata, scales')
testImage_jar, predata, scales = get_image.getImage(predict, BASE_DIR)
testfeature_jar = get_image.getFeature(config,testImage_jar)

fname = config['general']['UseFeature']
setName = config['general']['dataset']

num = int(lines[0].strip().split(' ')[6]) * 2
# print (num , len(testfeature_jar), len(part_data))
# # trainning model
print('Train, test')
est = list()
lrate = 0.03
k = 3

freq = 0.9
for index in range(0, num):
    # print (len(feature_jar['features.' + fname]), fname, len(part_data), index)
    x, y = load_data.getData(feature_jar['features.' + fname], part_data, index)
    print(type(x), '0000', len(y), y)
    est.append(GradientBoostingRegressor(n_estimators=500,
                                        learning_rate=lrate,
                                         max_depth=int(k),
                                         random_state=0,
                                         loss='ls').fit(x, y))
print("training over")
dirs = fname + setName + '/model'
if not os.path.exists(dirs):
    os.makedirs(dirs)

data = dirs + '/' + setName + fname + "_" + str(lrate) + "_" + str(k) + "500_1100.pkl";
print (data)
with open(data, "wb") as f:
    pickle.dump(est, f)
# est =pickle.load(open(data,'rb'))
ytest = []

for index in range(0, num):
    x, y = load_data.getData(testfeature_jar['features.' + fname], predata, index)
    # print(len(y), len(x), len(x[0]), index, len(est))
    temp = est[index].predict(x)
    ytest.append(temp)
yy = load_data.trans(ytest)
dirs = fname + setName + '/result'
if not os.path.exists(dirs):
    os.makedirs(dirs)

name = dirs + '/' + setName + fname + "_" + str(lrate) + "_" + str(k) + "500_1100.txt"
print(name)
file_object = open(name, 'w')
ind = 0
for y0 in yy:
    for y1 in y0:
        y1 = Decimal(y1 * scales[ind]).quantize(Decimal('0.000'))
        file_object.write(str(y1))
        file_object.write(' ')
    file_object.write('\r\n')
    ind = ind + 1
file_object.close()




