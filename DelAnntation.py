import io
import sys
import os
import xml.etree.ElementTree as ET
#sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#删除或者修改数据集某一类的xml文件
##修改下面的地址为你存放xml文件的位置，注意斜杠使用/,最后末尾需要加上/
#old_annotation是修要修改的标签名，new_annotation是修改后的标签名字
anno_path = 'F:/数据集/20190301输电线路主要缺陷负样本扩建数据集/Annotations/'
old_annotation = 'normal insulator'
new_annotation = 'normal single insulator'
del_annotations = ['strands defect']
#replace = True使用替换功能
#replace = False使用删除功能
REPLACE = True

def _main():
    filelist = os.listdir(anno_path)
    i = 0
    if REPLACE == True:
        for file in filelist:
            n_ = _Replace_Annotation(file)
            if n_ > 0:
                i += 1
    else:
        for file in filelist:
            n_ = _Del_Annotation(file)
            if n_ >0:
                i += 1
    print('the number of xmlfile is :' + str(i))


def _Replace_Annotation(filepath):
    if os.path.exists(anno_path + filepath) == False:
        print(filepath+' :not found')
    #建立xml树状结构
    i = 0
    while Replace_(filepath) == False:
        i += 1

    return i

def Replace_(filepath):
    if os.path.exists(anno_path + filepath) == False:
        print(filepath+' :not found')
    #建立xml树状结构
    tree = ET.parse(anno_path + filepath)
    #遍历xml文件 查找'name'
    for annoobject in tree.iter():
        if 'object' in annoobject.tag:
            for element in list(annoobject):
                if 'name' in element.tag:
                    #替换标签
                    if element.text == old_annotation:
                        element.text = new_annotation
                        print(filepath)
                        #重新写入xml，使修改生效
                        tree.write(anno_path+filepath, encoding="utf-8", xml_declaration=True)
                        return False
    return True

def _Del_Annotation(filepath):
    if os.path.exists(anno_path + filepath) == False:
        print(filepath+' :not found')
    #建立xml树状结构
    i = 0
    while Delete_(filepath) == False:
        i += 1
    return i
    
def Delete_(filepath):
    if os.path.exists(anno_path + filepath) == False:
        print(filepath+' :not found')
    #建立xml树状结构
    tree = ET.parse(anno_path + filepath)
    #遍历xml文件 查找'name'
    root = tree.getroot()
    for annoobject in root.iter():
        if 'object' in annoobject.tag:
            for element in list(annoobject):
                if 'name' in element.tag:
                    #删除标签
                    for anno in del_annotations:
                        if element.text == anno:
                            #从根节点下删除第一个子节点
                            root.remove(annoobject)
                            print(filepath)
                            #重新写入xml，使修改生效
                            tree = ET.ElementTree(root)
                            tree.write(anno_path+filepath, encoding="utf-8", xml_declaration=True)
                            return False
    return True

if __name__ == '__main__':
    _main()
