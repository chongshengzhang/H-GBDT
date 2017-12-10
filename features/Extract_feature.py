
from readInfo.read_img_Info import read_Img_info

class Extract_feat:
    def extract_all(self, images_file_path, feature_name):
#         read images_file_path
        print ("cccc");
        image_info_list = read_Img_info(images_file_path)
        return image_info_list
