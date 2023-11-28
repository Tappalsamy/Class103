import os
import shutil

source="C:/Users/trist/Downloads"
destination="C:/Users/trist/Downloads"

files=os.listdir(source)

for i in files:
    name,ext = os.path.splitext(i)
    
    if ext=="":
        continue
    if ext in [".txt",".pdf",".doc",".docx"]:
        path1=source+"/"+i
        path2=destination+"/documents"
        path3=destination+"/documents/"+i

        if os.path.exists(path2):
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            shutil.move(path1,path3)