import os.path
import glob
import re


if __name__ == "__main__":
    realpath = os.path.realpath(__file__)
    dirname = os.path.dirname(realpath)
    extension = 'jpg'
    file_list = glob.glob('*.'+extension)
    #在文件夹下面建立defectname.txt文档记录原始图像名称信息
    filetxt = open(os.path.join(dirname, 'defectname.txt'), 'w', encoding='utf-8')
    for index, filename in enumerate(file_list):
        #修改数字为起始标号
        index = index + 4643
        str_index = str(index)
        length = len(str_index)
        for i in range(6-length):
            str_index = '0' + str_index
        filepath = os.path.join(dirname, filename)
        newfilename = os.path.join(str_index, filename)
        print("%s\n" % (newfilename), file=filetxt)
        print(str_index + '.jpg')
        os.rename(filepath, str_index + '.jpg')
    filetxt.close()