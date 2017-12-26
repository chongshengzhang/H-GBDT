# H-GBDT （Henan University）
%  Facial Key Points Detection; 人脸关键点检测; 

#  对应论文:  基于GBDT和HOG特征的人脸关键点定位 （河南大学学报 自然科学版）  张重生 彭国雯  于珂珂*, 2017年10月投稿

%  已投稿论文：于珂珂学术论文-河大学报.pdf

% 主要开发人员： 于珂珂，河南大学硕士研究生。 其导师为 张重生.  本工作是于珂珂在张重生老师的指导下完成。

% 联系方式： 请同时发送邮件至： 于珂珂(1416560660@qq.com)  张重生(chongsheng.zhang@yahoo.com) 进行咨询


0. 依赖库：Scikit-learn,  numpy, OpenCV, Python Imaging Library (PIL).

1. 程序入口：test.py
在命令行中：python test.py即可
test.py中的lrate是GBDT的学习率，k是树的深度，lrate和k是GBDT中非常重要的参数。



2. 使用方法
config.ini中程序配置信息
    UseFeature：特征类型
    path：训练数据集路径
    dataset：数据集名称
    testSet：测试数据集路径
    
[features.gabor],[features.lbp]等是特征参数。该程序将生成后缀名为.pkl模型文件，和一个txt文件用于保存集的测试结果


3. 该程序的输入点和输出点皆是相对于人脸中心点信息。
   特征命名：
   单个特征：hog、gabor、lbp
   融合特征：gabor_hog、gabor_lbp、hog_lbp
   级联特征：gaborHog、lbpHog、lbpgabor

4. BioidErrResult.py 检测误差平均值

------------------
详见H-GBDT-Master使用文档。

                           H-GBDT 使用文档
            本文档由河南大学大数据研究中心2017级硕士研究生-付飞飞-验证整理
            
1.	安装python环境
建议下载安装anaconda，在官网（https://www.anaconda.com/download/
）下载对应的版本，本文以Windows10+python3.5为例。
 
双击下载完成后的Anaconda3-5.0.1-Windows-x86_64.exe文件，进行安装。一直点下一步即可。

 
安装完成后，打开windows的命令提示符：
输入conda list 就可以查询现在安装了哪些库，常用的numpy, scipy名列其中。如果你还有什么包没有安装上，可以运行
conda install ***  来进行安装。（***为需要的包的名称，例如conda install numpy）
如果某个包版本不是最新的，运行 conda update *** 就可以更新了。
在cmd中输入python，可以看到如下信息，至此python安装完成。
 

2.	使用pip安装依赖库Scikit-learn+numpy+OpenCV+Python Imaging Library (PIL)
pip install Scikit-learn 
Pip install numpy 
pip install opencv-python 
pip install PIL


3.	在控制台输入python test.py进行测试。
【注意：
python3.*环境中，feature_gabor.py可能会出错，如果出现以下错误
ModuleNotFoundError: No module named 'base_feature'

可以把from base_feature import BaseFeature改为
from .base_feature import BaseFeature as BaseFeature 
】

Ubantu下同上。
