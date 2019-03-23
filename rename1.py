import os.path
import glob
import re
#将图片文件的名字重新编号
#图像文件夹地址
path = 'F:/张珂老师巡检图像/第二次缺陷图像 - 副本/'
text_path = 'f:/'
if __name__ == "__main__":
    '''realpath = os.path.realpath(__file__)
    dirname = os.path.dirname(realpath)
    extension = 'jpg'
    file_list = glob.glob('*.'+extension)'''
    file_list = os.listdir(path)
    #在文件夹下面建立defectname.txt文档记录原始图像名称信息
    filetxt = open(os.path.join(text_path, 'defectname.txt'), 'w', encoding='utf-8')
    for index, filename in enumerate(file_list):
        #修改数字为起始标号
        index = index + 7507
        str_index = str(index)
       # length = len(str_index)
       # for i in range(6-length):
       #     str_index = '7507' + str_index
        filepath = os.path.join(path, filename)
        newfilename = os.path.join(str_index, filename)
        print("%s\n" % (newfilename), file=filetxt)
        print(str_index + '.jpg')
        os.rename(filepath, path + str_index + '.jpg')
    filetxt.close()