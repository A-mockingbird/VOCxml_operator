from PIL import Image
from pylab import *
import os
import xml.etree.ElementTree as ET

#将数据集中的标注框从图片中剪裁出来
####anno_path存放xml文件，image_path存放未剪裁图片，crop_path存放剪裁后图片
anno_path = 'C:/Users/91279/Desktop/何颖宣 19.2.20/金具/xml/'
image_path = 'C:/Users/91279/Desktop/何颖宣 19.2.20/金具/images/'
crop_path = 'C:/Users/91279/Desktop/何颖宣 19.2.20/金具/crop/'


def _main():
    filelist = os.listdir(anno_path)
    all_annotation = 0
    all_image = 0
    for file in filelist:
        num, annos = _ParseAnnotation(file)
        #annotation_num = _crop(num, annos, file)
        #all_annotation = all_annotation + annotation_num
        #all_image+=1
        i = 0
        for j in range(num):
            i += 1
            _crop(i, annos[j], file)
            print(file)
        all_image+=1
    print(all_image)

def _ParseAnnotation(filepath):
    if os.path.exists(anno_path + filepath) == False:
        print(filepath+' :not found')
    tree = ET.parse(anno_path + filepath)
    annos = [None]*30
    num = 0 
    for annoobject in tree.iter():
        if 'object' in annoobject.tag:
            for element in list(annoobject):
                if 'name' in element.tag:
                    name = element.text 
                if 'bndbox' in element.tag:
                    for size in list(element):
                        if 'xmin' in size.tag:
                            xmin = size.text
                        if 'ymin' in size.tag:
                            ymin = size.text
                        if 'xmax' in size.tag:
                            xmax = size.text
                        if 'ymax' in size.tag:
                            ymax = size.text
                            annos[num] = {'name':name, 'xmin':int(xmin), 'ymin':int(ymin), 'xmax':int(xmax), 'ymax':int(ymax)}
                            #annos[num] = {'name':name, 'xmin':xmin, 'ymin':ymin, \
                             #           'xmax':xmax, 'ymax':ymax}                     
                            num += 1
    return num, annos

def _crop(num, annotation, file):
    filenum = os.path.splitext(file)
    filename = filenum[0] + '.jpg'
    if os.path.exists(image_path + filename) != True:
        print(filename + 'not found')
        return
    box = (annotation['xmin'], annotation['ymin'], annotation['xmax'], annotation['ymax'])
    pil_im = Image.open(image_path + filename)
    region = pil_im.crop(box)
    pil_region = Image.fromarray(uint8(region))
    pil_region.save(crop_path + annotation['name']+filenum[0]+'_'+str(num)+'.jpg')

if __name__ == '__main__':
    _main()
