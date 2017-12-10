# -*- coding: UTF-8 -*-

import skimage
import skimage.feature
from base_feature import BaseFeature


class FeatureGaborhog(BaseFeature):
    def __init__(self, config):
        super(FeatureGaborhog, self).__init__(config)
        # Which layer should be used
        self.layer = 'gray'
        # The extractor here is a function but a variable
        self.extractor = skimage.feature.hog


    def extract_one(self, image):
        # print (self.config['frequency'], self.config['fre'], self.config['fre'])
        feature_lbp, foo = skimage.filters.gabor(image,frequency = float(self.config['frequency']))

        feature = self.extractor(feature_lbp, pixels_per_cell=(int(self.config['pixels_per_cell_x']),
                                                               int(self.config['pixels_per_cell_y'])),
                                              cells_per_block=(int(self.config['cells_per_block_x']),
                                                               int(self.config['cells_per_block_y'])))
        if bool(self.config['ravel']):
            feature = feature.ravel()
        # print(feature)
        return feature
