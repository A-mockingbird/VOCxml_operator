import os.path
import glob

#将图片jpg文件后缀小写或者大写

if __name__ == "__main__":
    realpath = os.path.realpath(__file__)
    dirname = os.path.dirname(realpath)
    extension = 'JPG'
    file_list = glob.glob('*.'+extension)
    for filename in file_list:
        #如果想要全部大写，改成lowerfilename = filename.upper()
        lowerfilename = filename.lower()
        filepath = os.path.join(dirname, filename)
        os.rename(filepath, lowerfilename)
        print(lowerfilename)