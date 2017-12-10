# -*- coding: UTF-8 -*-

import skimage
import skimage.feature

__author__ = 'Hao Yu'


class BaseFeature(object):
    def __init__(self, config=None):
        self.layer = 'rgb'
        self.config = config
        self.extractor = None

    def extract_all(self, image_jar):
        features = list()
        # print (self.layer)
        for image in image_jar[self.layer]:
            features.append(self.extract_one(image))
        return features

    def extract_one(self, image):
        # This function should be override by subclass
        return None
