import math
import xlwt
import numpy as np
# from writeInfo import writeXlsx

def twoArray(workbook, tableName, data):

    worksheet = workbook.add_sheet(tableName)
    # for i in range(0, len(title)):
    #     worksheet.write(0, i, label=title[i]);

    print (len(data), len(data[0]))
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            # print (data[i][j])
            worksheet.write(i, j, label=data[i][j])



workbook = xlwt.Workbook(encoding='ascii')
#
# real = open("Files/lfpw_test.txt").readlines()
# # name = "ldohoglfw/result/lfwldohog_0.03_3.txt"
# # real = open("lfpw_helen/lfpw_test.txt").readlines()
# # name = "ldohoglfpw/result/lfpwldohog_0.03_3.txt"
# # real = open("Files/lTest.txt").readlines()
# # name = "lfwDlibresult.txt"
# # real = open("Files/BioID_test.txt").readlines()
# # name = "ldohoglfpwrandom/result/lfpwldohog_0.14_4.txt"
# # name = "Files/BioID_result111100.txt"
# # name= 'lfpwSOFR/lfpwSOFR_result13.txt'
# # name='LFWResult/LFWBioID11.txt'
# # name = "ldohoglfpwrandom/result/lfpwldohog_0.14_4.txt"
# # name = 'hoglfwrandom/result/lfwhog_0.14_4.txt'
# name = 'lbpgaborlfpw/result/lfpwlbpgabor_0.030.9_2500.txt'

real = open("Files/lfwTest.txt").readlines()
# name = "ldohoglfw/result/lfwldohog_0.03_3.txt"
# real = open("lfpw_helen/lfpw_test.txt").readlines()
# name = "ldohoglfpw/result/lfpwldohog_0.03_3.txt"
# real = open("Files/lTest.txt").readlines()
# name = "lfwDlibresult.txt"
# real = open("Files/BioID_test.txt").readlines()
# name = "ldohoglfpwrandom/result/lfpwldohog_0.14_4.txt"
# name = "Files/BioID_result111100.txt"
# name= 'lfpwSOFR/lfpwSOFR_result13.txt'
# name='LFWResult/LFWBioID11.txt'
# name = "ldohoglfpwrandom/result/lfpwldohog_0.14_4.txt"
# name = 'hoglfwrandom/result/lfwhog_0.14_4.txt'
name = 'gabor_hoglfw/result/lfwgabor_hog_0.030.9_21500.txt'
predict = open(name).readlines()
print(len(predict))
print (name)


# error = []
print (len(predict), len(real))
err = []
everyFace = []
# sum = 0
# error = 0
for i, line in enumerate(real):
    r = map(float, line.strip().split(" ")[1:])
    p = map(float, predict[i].strip().split(" "))
    # print (p)
    # for
    rx = r[6::2]
    ry = r[7::2]
    px = p[0::2]
    py = p[1::2]
    # width = r[2]
    # x =
    er = []

    # dis = math.sqrt((rx[1] - rx[0]) **2 + (ry[1] - ry[0]) ** 2)
    # sum = sum + dis
    # print (dis)ldohoglfwrandom/result/lfwldohog_2.txt

    for k in xrange(18):
        # e = math.sqrt((rx[k] - px[k] + r[0] + r[2]/2.0 ) ** 2 + (ry[k] - py[k] + r[1] + r[2]/2.0 ) ** 2)
        # e = math.sqrt((round()rx[k] - px[k] + r[0] + r[2] / 2.0) ** 2 + (ry[k] - py[k] + r[1] + r[2] / 2.0) ** 2)
        # e = math.sqrt((round(rx[k]) - round(px[k]) + round(r[0]) + round(r[2]) / 2.0) ** 2 + (
        # round(ry[k]) - round(py[k]) + round(r[1]) + round(r[2]) / 2.0) ** 2)
        # e = math.sqrt((ry[k] - py[k]) ** 2)
        # print(rx[k] , px[k])
        # e = math.sqrt((rx[k] - px[k] - r[0] - r[2] / 2.0) ** 2 + (ry[k] - py[k] - r[1] - r[2] / 2.0) ** 2)
        e = math.sqrt((rx[k] - px[k]) ** 2 + (ry[k] - py[k]) ** 2)
        e = e*100/float(r[3])
        # e = e*100/dis
        # error = error + e/

        er.append(e)
    # print (er)
    everyFace.append(np.mean(er))
    err.append(er)
#
# print (error *100/(18*sum), sum, error)
# print (everyFace)
t = map(list, zip(*err))
for i in xrange(len(t)):
    print (i, round(np.mean(t[i]), 4))
    num = 3
    # print(round(np.mean(t[i]), 4), len([x for x in t[i] if x <= num])/float(len(t[i])))

mean = np.mean(err)
print ("mean: ", mean)


# print np.sum(everyFace >5,keepdims=True)
num = 3
print (len([x for x in everyFace if x <= num]),len([x for x in everyFace if x <= num])/float(len(everyFace)))

# lines = open("lfpw_helen/lfpw_train.txt").readlines()
# wf = open('lfpw_helen/train.txt', 'wb')
# for line in lines:
#     data = line.strip().split(' ')
#     wf.writelines(data[0] + "\n")
# wf.close()
#
#
# lines = open("lfpw_helen/lfpw_test.txt").readlines()
# wf = open('lfpw_helen/test.txt', 'wb')
# for line in lines:
#     data = line.strip().split(' ')
#     wf.writelines(data[0] + "\n")
# wf.close()
#













