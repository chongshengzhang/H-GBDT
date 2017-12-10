# -*- coding: UTF-8 -*-

import skimage
import skimage.feature
from .base_feature import BaseFeature


class FeatureLbp(BaseFeature):
    def __init__(self, config):
        super(FeatureLbp, self).__init__(config)
        # super().__init__(config)
        # Which layer should be used
        self.layer = 'gray'
        # The extractor here is a function but a variable
        self.extractor = skimage.feature.local_binary_pattern

    def extract_one(self, image):
        # Extract feature
        feature = self.extractor(image,
                                 P=int(self.config.get('P', 32)),
                                 R=int(self.config.get('R', 1)),
                                 method=self.config.get('method', 'nri_uniform')
                                 )
        # Expend it?
        if bool(self.config.get('ravel', True)):
            feature = feature.ravel()

        return feature
