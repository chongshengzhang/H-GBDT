# -*- coding: UTF-8 -*-

import skimage
import skimage.feature
from .base_feature import BaseFeature




class FeatureHog(BaseFeature):
    def __init__(self, config):
        # BaseFeature().__init__(config)
        super(FeatureHog, self).__init__(config)
        # Which layer should be used
        self.layer = 'gray'
        # The extractor here is a function but a variable
        self.extractor = skimage.feature.hog

    def extract_one(self, image):
        # Extract feature
        feature = self.extractor(image,
                                 pixels_per_cell=(int(self.config.get('pixels_per_cell_x')),
                                                  int(self.config.get('pixels_per_cell_y'))),
                                 cells_per_block=(int(self.config.get('cells_per_block_x')),
                                                  int(self.config.get('cells_per_block_y')))
                                 )
        # print (feature)
        # Expend it?
        if bool(self.config.get('ravel', True)):
            feature = feature.ravel()
            # print('hog', len(feature))
        return feature
