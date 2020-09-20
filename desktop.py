
import os
import shutil
filepath = r"C:\Users\zhiwe\Desktop\\"
dirpath = r"F:\桌面\\"

#shutil.move(files, dirpath)

for filename in os.listdir(filepath):
    
    fs = filepath + filename
    #print(fs)
    if filename.endswith(".doc") or filename.endswith(".pdf") or filename.endswith(".docx") or filename.endswith(".xls") or filename.endswith(".xlsx") or filename.endswith(".txt"):
        shutil.move(fs, dirpath+"文档")
    elif filename.endswith(".avi") or filename.endswith(".mp4"):
        shutil.move(fs, dirpath+"视频")
    elif filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".bmp"):
        shutil.move(fs, dirpath+"图片")
    elif filename.endswith(".dwg") or filename.endswith(".3dm") or filename.endswith(".exb") or filename.endswith(".bak"):
        shutil.move(fs, dirpath+"图纸")    
    elif filename.endswith(".rar") or filename.endswith(".zip") or filename.endswith(".7z"):
        shutil.move(fs, dirpath+"压缩")     
    elif filename.endswith(".lnk"):
        if filename not in "桌面OS.lnk":
            shutil.move(fs, dirpath+"快捷方式")     
    elif filename.endswith(".exe"):
        shutil.move(fs, dirpath+"安装包")     
    elif os.path.isdir(fs) == True:
        if os.listdir(fs) != []:
            print("=========================================")
            print(os.listdir(fs))
            shutil.move(fs, dirpath+"目录")
print("----------------------------------")


    