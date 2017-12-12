import os

def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    nameList = []
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        nameList.append(child.decode('gbk'))
        # print (child)# .
    return nameList