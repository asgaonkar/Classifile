#ps aux | grep -ie "python3 Class" | grep "Tl" | awk '{print $2}' | xargs kill -9

import os
import sys
import time
import fnmatch
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, LoggingFileSystemEventHandler, FileSystemEventHandler


class SourceHandler(FileSystemEventHandler):

    def on_modified(self, event):

        #Recursively find all files and directories
        for root, dirs, files in os.walk(src_folder, topdown=False):

            #Move all the files to their respective folders
            for filename in files:
                file_path = os.path.join(root, filename)
                print("File: {}".format(file_path))
                logger.debug("Removed \'{}\'".format(file_path))
                #os.remove(file_path) #Move the file and Log it


            #Delete all empty folders
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                print("Folder: {}".format(dir_path))
                # os.rmdir(dir_path)
        return


class ChangedHandler(FileSystemEventHandler):

    def on_modified(self, event):
        print("Hi")
        return



#For Root Logger
#logging.basicConfig(filename='Classifile.log',level=logging.NOTSET,format='%(asctime)s:%(created)f:%(funcName)s:%(levelname)s:%(message)s')

curr_dir = os.getcwd()


src_folder = os.sys.argv[1]
dst_folder = os.sys.argv[2]
log_folder = os.sys.argv[3]

if(not(os.path.isdir(src_folder))):
    try:
        os.mkdir(src_folder,0o666)
    except FileExistsError:
        pass

if(not(os.path.isdir(dst_folder))):
    try:
        os.mkdir(dst_folder,0o666)
    except FileExistsError:
        pass

if(not(os.path.isdir(log_folder))):
    try:
        os.mkdir(log_folder,0o666)
    except FileExistsError:
        pass

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
format_str = '%(asctime)s : %(created)f : %(funcName)s : %(message)s'
date_format = '%Y-%m-%D %H:%M:%S'
formatter = logging.Formatter(format_str,date_format)
source_log_file = log_folder + '/Source.log'
file_handler = logging.FileHandler(source_log_file)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

changed_logger = logging.getLogger(__name__)
changed_logger.setLevel(logging.DEBUG)
changed_log_file = log_folder + '/Category.log'
changed_file_handler = logging.FileHandler(changed_log_file)

observer = Observer()
event = SourceHandler()
observer.schedule(event,src_folder,recursive=True)
observer.start()

changed_observer = Observer()
changed_event = ChangedHandler()
changed_observer.schedule(changed_event,dst_folder,recursive=True)
changed_observer.start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    observer.stop()
    changed_observer.stop()
observer.join()
changed_observer.join()
