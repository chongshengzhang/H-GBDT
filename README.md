# H-GBDT （Henan University）
%  Facial Key Points Detection; 人脸关键点检测; 

#  对应论文:  基于GBDT和HOG特征的人脸关键点定位 （河南大学学报 自然科学版）  张重生 彭国雯  于珂珂*, 2017年10月投稿

% 主要开发人员： 于珂珂，河南大学硕士研究生。 其导师为 张重生.  本工作是于珂珂在张重生老师的指导下完成。

% 联系方式： 请同时发送邮件至： 于珂珂(1416560660@qq.com)  张重生(chongsheng.zhang@yahoo.com) 进行咨询


0. 依赖库：scikit-learn， numpy， PIL库.

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
