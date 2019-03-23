import os
SourceDir = 'F:/张珂老师巡检图像/new gradingring/xml/'
DestDir = 'F:/张珂老师巡检图像/new gradingring/images/'

if __name__ == '__main__':
    all_fileName = os.listdir(SourceDir)
    k=0
    for fileName in all_fileName:
        suffix = fileName[-4:].lower()
        if suffix == ".xml":
            if not os.path.exists(os.path.join(DestDir, fileName[0:-4]+".jpg")):
                print(fileName)
                os.remove(os.path.join(SourceDir, fileName))  # 删除文件
            else:k=k+1
    print(str(k))

    all_fileName = os.listdir(DestDir)
    k=0
    for fileName in all_fileName:
        suffix = fileName[-4:].lower()
        if suffix == ".jpg":
            if not os.path.exists(os.path.join(SourceDir, fileName[0:-4]+".xml")):
                print(fileName)
                os.remove(os.path.join(DestDir, fileName))  # 删除文件
            else:k=k+1
    print(str(k))
