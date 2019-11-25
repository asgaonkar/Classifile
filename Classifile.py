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
                #logger.debug("Removed \'{}\'".format(file_path)) #Fix the logger
                try:
                    fullfile, file_extension = os.path.splitext(file_path)
                except Exception as e:
                    file_extension = 'noname'

                dst_path_folder = os.path.join(dst_folder,extensions_folders[file_extension])
                print("Move to {}".format(dst_path_folder))

                #Create chain directory until the desired folder
                os.makedirs(dst_path_folder, 0o666, exist_ok=True)
                dst_path = os.path.join(dst_path_folder,filename)

                #Move the file and Log it
                os.rename(file_path,dst_path)


            #Delete all empty folders
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                print("Folder: {}".format(dir_path))

                #Delete the folder and Log it
                os.rmdir(dir_path)
        return


class ChangedHandler(FileSystemEventHandler):

    def on_modified(self, event):
        print("Hi")
        return



#For Root Logger
#logging.basicConfig(filename='Classifile.log',level=logging.NOTSET,format='%(asctime)s:%(created)f:%(funcName)s:%(levelname)s:%(message)s')

extensions_folders = {
#No name
    'noname' : "Other/Uncategorized",
#Audio
    '.aif' : "Media/Audio",
    '.cda' : "Media/Audio",
    '.mid' : "Media/Audio",
    '.midi' : "Media/Audio",
    '.mp3' : "Media/Audio",
    '.mpa' : "Media/Audio",
    '.ogg' : "Media/Audio",
    '.wav' : "Media/Audio",
    '.wma' : "Media/Audio",
    '.wpl' : "Media/Audio",
    '.m3u' : "Media/Audio",
#Text
    '.txt' : "Text/TextFiles",
    '.doc' : "Text/Microsoft/Word",
    '.docx' : "Text/Microsoft/Word",
    '.odt ' : "Text/TextFiles",
    '.pdf': "Text/PDF",
    '.rtf': "Text/TextFiles",
    '.tex': "Text/TextFiles",
    '.wks ': "Text/TextFiles",
    '.wps': "Text/TextFiles",
    '.wpd': "Text/TextFiles",
#Video
    '.3g2': "Media/Video",
    '.3gp': "Media/Video",
    '.avi': "Media/Video",
    '.flv': "Media/Video",
    '.h264': "Media/Video",
    '.m4v': "Media/Video",
    '.mkv': "Media/Video",
    '.mov': "Media/Video",
    '.mp4': "Media/Video",
    '.mpg': "Media/Video",
    '.mpeg': "Media/Video",
    '.rm': "Media/Video",
    '.swf': "Media/Video",
    '.vob': "Media/Video",
    '.wmv': "Media/Video",
#Images
    '.ai': "Media/Images",
    '.bmp': "Media/Images",
    '.gif': "Media/Images",
    '.ico': "Media/Images",
    '.jpg': "Media/Images",
    '.jpeg': "Media/Images",
    '.png': "Media/Images",
    '.ps': "Media/Images",
    '.psd': "Media/Images",
    '.svg': "Media/Images",
    '.tif': "Media/Images",
    '.tiff': "Media/Images",
    '.CR2': "Media/Images",
#Internet
    '.asp': "Other/Internet",
    '.aspx': "Other/Internet",
    '.cer': "Other/Internet",
    '.cfm': "Other/Internet",
    '.cgi': "Other/Internet",
    '.pl': "Other/Internet",
    '.css': "Other/Internet",
    '.htm': "Other/Internet",
    '.js': "Other/Internet",
    '.jsp': "Other/Internet",
    '.part': "Other/Internet",
    '.php': "Other/Internet",
    '.rss': "Other/Internet",
    '.xhtml': "Other/Internet",
#Compressed
    '.7z': "Other/Compressed",
    '.arj': "Other/Compressed",
    '.deb': "Other/Compressed",
    '.pkg': "Other/Compressed",
    '.rar': "Other/Compressed",
    '.rpm': "Other/Compressed",
    '.tar.gz': "Other/Compressed",
    '.z': "Other/Compressed",
    '.zip': "Other/Compressed",
#Disc
    '.bin': "Other/Disc",
    '.dmg': "Other/Disc",
    '.iso': "Other/Disc",
    '.toast': "Other/Disc",
    '.vcd': "Other/Disc",
#Data
    '.csv': "Programming/Database",
    '.dat': "Programming/Database",
    '.db': "Programming/Database",
    '.dbf': "Programming/Database",
    '.log': "Programming/Database",
    '.mdb': "Programming/Database",
    '.sav': "Programming/Database",
    '.sql': "Programming/Database",
    '.tar': "Programming/Database",
    '.xml': "Programming/Database",
    '.json': "Programming/Database",
#Executables
    '.apk': "Other/Executables",
    '.bat': "Other/Executables",
    '.com': "Other/Executables",
    '.exe': "Other/Executables",
    '.gadget': "Other/Executables",
    '.jar': "Other/Executables",
    '.wsf': "Other/Executables",
#Fonts
    '.fnt': "Other/Fonts",
    '.fon': "Other/Fonts",
    '.otf': "Other/Fonts",
    '.ttf': "Other/Fonts",
#Presentations
    '.key': "Text/Presentations",
    '.odp': "Text/Presentations",
    '.pps': "Text/Presentations",
    '.ppt': "Text/Presentations",
    '.pptx': "Text/Presentations",
#Programming
    '.c': "Programming/C&C++",
    '.class': "Programming/Java",
    '.dart': "Programming/Dart",
    '.py': "Programming/Python",
    '.sh': "Programming/Shell",
    '.swift': "Programming/Swift",
    '.html': "Programming/C&C++",
    '.h': "Programming/C&C++",
#Spreadsheets
    '.ods' : "Text/Microsoft/Excel",
    '.xlr' : "Text/Microsoft/Excel",
    '.xls' : "Text/Microsoft/Excel",
    '.xlsx' : "Text/Microsoft/Excel",
#System
    '.bak' : "Text/Other/System",
    '.cab' : "Text/Other/System",
    '.cfg' : "Text/Other/System",
    '.cpl' : "Text/Other/System",
    '.cur' : "Text/Other/System",
    '.dll' : "Text/Other/System",
    '.dmp' : "Text/Other/System",
    '.drv' : "Text/Other/System",
    '.icns' : "Text/Other/System",
    '.ico' : "Text/Other/System",
    '.ini' : "Text/Other/System",
    '.lnk' : "Text/Other/System",
    '.msi' : "Text/Other/System",
    '.sys' : "Text/Other/System",
    '.tmp' : "Text/Other/System",
}

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
