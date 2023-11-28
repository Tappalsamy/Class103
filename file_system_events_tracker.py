import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/trist/Downloads"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src._path} has been created.")
    
    def on_deleted(self, event):
        print(f"Someone deleted {event.src_path}.")

    def on_moved(self, event):
        print(f"Someone has moved {event.src._path}.")
    
    def on_modified(self, event):
        print(f"Someone has modified {event.src._path}.")

eventHandler = FileEventHandler()
obs = Observer()
obs.schedule(eventHandler,from_dir,recursive=True)
obs.start()

try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stopped")
    obs.stop()
