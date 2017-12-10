# -*- coding: UTF-8 -*-

import skimage
import skimage.feature
from base_feature import BaseFeature


class FeatureLbphog(BaseFeature):
    def __init__(self, config):
        super(FeatureLbphog, self).__init__(config)
        # Which layer should be used
        self.layer = 'gray'
        # The extractor here is a function but a variable
        self.extractor = skimage.feature.hog


    def extract_one(self, image):
        feature_lbp = skimage.feature.local_binary_pattern(image,
                                                           P=int(self.config.get('P')),
                                                           R=int(self.config.get('R')),
                                                           method=self.config.get('method'))

        feature = self.extractor(feature_lbp,

                                              pixels_per_cell=(int(self.config.get('pixels_per_cell_x')),
                                                               int(self.config.get('pixels_per_cell_y'))),
                                              cells_per_block=(int(self.config.get('cells_per_block_x')),
                                                               int(self.config.get('cells_per_block_y'))))
        if bool(self.config.get('ravel')):
            feature = feature.ravel()
        # print(feature)
        return feature
