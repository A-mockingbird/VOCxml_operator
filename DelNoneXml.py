from PIL import Image
from pylab import *
import os
import xml.etree.ElementTree as ET

#删除数据集中空的xml文件
anno_path = 'F:/数据集/20190301输电线路主要缺陷负样本扩建数据集/Annotations/'
DELNUM = 0

def _main():
    filelist = os.listdir(anno_path)
    all_annotation = 0
    all_image = 0
    for file in filelist:
        _DelNoneAnnotation(file)
    print(DELNUM)

def _DelNoneAnnotation(filepath):
    if os.path.exists(anno_path + filepath) == False:
        print(filepath+' :not found')
    tree = ET.parse(anno_path + filepath)
    num = 0
    for annoobject in tree.iter():
        if 'object' in annoobject.tag:
           num += 1
    if num==0:
        os.remove(anno_path + filepath)
        print(filepath)
        global DELNUM
        DELNUM += 1

if __name__ == '__main__':
    _main()
