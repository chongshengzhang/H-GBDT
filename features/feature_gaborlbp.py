# -*- coding: UTF-8 -*-

import skimage
import skimage.feature
from base_feature import BaseFeature


class FeatureGaborlbp(BaseFeature):
    def __init__(self, config):
        super(FeatureGaborlbp, self).__init__(config)
        # Which layer should be used
        self.layer = 'gray'
        # The extractor here is a function but a variable
        self.extractor = skimage.feature.local_binary_pattern


    def extract_one(self, image):
        # print (self.config['frequency'], self.config['fre'], self.config['fre'])
        feature_lbp, foo = skimage.filters.gabor(image,frequency = float(self.config['frequency']))

        # feature = self.extractor(feature_lbp, pixels_per_cell=(int(self.config['pixels_per_cell_x']),
        #                                                        int(self.config['pixels_per_cell_y'])),
        #                                       cells_per_block=(int(self.config['cells_per_block_x']),
        #                                                        int(self.config['cells_per_block_y'])))

        feature = self.extractor(feature_lbp,
                                 P=int(self.config.get('P')),
                                 R=int(self.config.get('R')),
                                 method=self.config.get('method', 'nri_uniform')
                                 )
        if bool(self.config['ravel']):
            feature = feature.ravel()
        # print(feature)
        return feature
