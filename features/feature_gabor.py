# -*- coding: UTF-8 -*-

import skimage
import skimage.filters
from base_feature import BaseFeature

__author__ = 'Hao Yu'


class FeatureGabor(BaseFeature):
    def __init__(self, config):
        # BaseFeature().__init__(config)
        super(FeatureGabor, self).__init__(config)
        # Which layer should be used
        self.layer = 'gray'
        # The extractor here is a function but a variable
        self.extractor = skimage.filters.gabor

    def extract_one(self, image):
        # Extract feature
        # print(self.config.get('frequency', 0.1))
        foo, feature = self.extractor(image, frequency = float(self.config.get('frequency', 0.1))
                                      )
        # Expend it?
        if bool(self.config.get('ravel', True)):
            feature = feature.ravel()

        return feature
