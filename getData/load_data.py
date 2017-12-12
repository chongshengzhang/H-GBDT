import numpy as np

def float_data(lines):
    data = []
    for line in lines:
        str = line.split(' ')[5::]
        temp = []
        for s in str:
            temp.append(float(s))
        data.append(temp)
        # print(temp)
    return data

def getData(feature, part_data, index):
    x = [];
    y = [];
    i = 0;
    # print(part_data[1] ,'9090909')
    # print (feature, 'lklkjlkjl', len(feature))

    for fe in feature:
        x.append(fe)

        # print (i, ' ,.,.,.,.,,.,,,,,,,' , index)
        y.append(part_data[i][index])
        i = i+1
    # print (len(x), len(y))
    return x, y

def trans(m):
    a = [[] for i in m[0]]
    for i in m:
        for j in range(len(i)):
            a[j].append(i[j])
    return a

def getMulData(feature, part_data, index):
    x = [];
    y = [];
    i = 0;
    # print(part_data[1][index])
    for fe in feature:
        x.append(fe)
        # print(part_data[i][index*2], part_data[i][index*2 + 1], index)
        e = [part_data[i][index*2], part_data[i][index*2 + 1]];
        y.append(e)
        i = i+1
    return x, y

#
# def getMixData(feature, part_data, index):
#     x = [];
#     y = [];
#     i = 0;
#     for k in range(0,len(feature)):
#         if k>=len(part_data):
#             i = k%len(part_data)
#             # print (k, i,len(x[i]), len(feature[k]), type(x[i]), type(feature[k]))
#             if k>= 2*len(part_data):
#                 temp = x[i].tolist() + feature[k].tolist()
#             else:
#                 # print ('xvccbv');
#                 temp = x[i] + feature[k].tolist()
#             x[i] = np.array(temp)
#             # print (len(x[i]),type(x[i]),type(feature[k]), len(x),len(feature))
#         else:
#             x.append(feature[k].tolist())
#             y.append(part_data[k][index])
#     return x, y



