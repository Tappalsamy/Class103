import random
import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source="C:/Users/trist/Downloads"
destination="C:/Users/trist/Downloads"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,ext = os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            if ext in value:
                filename = os.path.basename(event.src_path)
                print("Downloaded",filename)
                path1=source+"/"+filename
                path2=destination+"/"+key
                path3=destination+"/"+key+"/"+filename

                if os.path.exists(path2):
                    shutil.move(path1,path3)
                else :
                    os.makedirs(path2)
                    shutil.move(path1,path3)


eventHandler = FileMovementHandler()
obs = Observer()
obs.schedule(eventHandler,source,recursive=True)
obs.start()

try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stopped")
    obs.stop()