# -*- coding: UTF-8 -*-

import os

import django.conf
import dlib
import numpy as np

from .base_feature import BaseFeature

__author__ = 'Hao Yu'


class FeatureLandmark(BaseFeature):
    extractor = dlib.shape_predictor(
        os.path.join(django.conf.settings.SAVE_DIR['MODEL'],
                     'feature_landmark',
                     'face_landmark.dat')      #### 找关键点
    )
    default_param = None
    layer = 'gray'

    box = dlib.rectangle(left=0, top=0, right=255, bottom=255)

    @classmethod
    def extract(cls, picture=None, params = default_param):
        feature = []
        landmarks = cls.extractor(picture, cls.box)
        for point in landmarks.parts():
            feature.append(point.x)
            feature.append(point.y)

        return np.array(feature).ravel()
