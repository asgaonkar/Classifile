import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, LoggingFileSystemEventHandler, FileSystemEventHandler


class SourceHandler(FileSystemEventHandler):

    def on_modified(self, event):
        return


class ChangedHandler(FileSystemEventHandler):

    def on_modified(self, event):
        return



#For Root Logger
#logging.basicConfig(filename='Classifile.log',level=logging.NOTSET,format='%(asctime)s:%(created)f:%(funcName)s:%(levelname)s:%(message)s')

curr_dir = os.getcwd()


src_folder = os.sys.argv[1]
dst_folder = os.sys.argv[2]
log_folder = os.sys.argv[3]

if(not(os.path.isdir(src_folder))):
    os.mkdir(src_folder,0o666)

try:
    os.mkdir(log_folder,0o666)
    os.mkdir(dst_folder,0o666)
except FileExistsError:
    pass

logger = logging.getLogger(__name__)
logger.setLevel(logging.NOTSET)
format_str = '%(asctime)s : %(created)f : %(funcName)s : %(levelname)s : %(message)s'
date_format = '%Y-%m-%D %H:%M:%S'
formatter = logging.Formatter(format_str,date_format)
source_log_file = log_folder + '/Source.log'
file_handler = logging.FileHandler(source_log_file)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

changed_logger = logging.getLogger(__name__)
changed_logger.setLevel(logging.NOTSET)
changed_log_file = log_folder + '/Category.log'
changed_file_handler = logging.FileHandler(changed_log_file)


observer = Observer()
event = SourceHandler()
observer.schedule(event,src_folder,recursive=True)
observer.start()

changed_observer = Observer()
changed_event = ChangedHandler()
changed_observer.schedule(changed_event,dst_folder,recursive=True)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
