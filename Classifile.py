#To kill recurring tasks that wasnt properly closed. Use at personal risk.
#ps aux | grep -ie "python3 Class" | grep "Tl" | awk '{print $2}' | xargs kill -9

import os
import sys
import time
import fnmatch
import logging
import argparse
import datetime
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, LoggingFileSystemEventHandler, FileSystemEventHandler

parser = argparse.ArgumentParser(description='Classifile:')
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-s", "--src", required=True, type=str, help="Sorce Folder (path)")
requiredNamed.add_argument("-d", "--dst", required=True, type=str, help="Destination Folder (path)")
requiredNamed.add_argument("-l", "--log", required=True, type=str, help="Log Folder (path)")
args = parser.parse_args()


class SourceHandler(FileSystemEventHandler):

    def on_modified(self, event):

        #Recursively find all files and directories
        for root, dirs, files in os.walk(src_folder, topdown=False):

            #Move all the files to their respective folders
            for filename in files:
                file_path = os.path.join(root, filename)
            
                #logger.debug("Removed \'{}\'".format(file_path)) #Fix the logger (v2.0)

                try:
                    fullfile, file_extension = os.path.splitext(file_path)
                except:
                    file_extension = 'noname'

                currentMonth = datetime.datetime.now().strftime("%B")
                currentYear = datetime.datetime.now().year


                dst_path_folder = os.path.join(dst_folder,extensions_folders[file_extension])
                

                #Create chain directory until the desired folder
                dst_path_folder = os.path.join(dst_path_folder,str(currentYear))
                dst_path_folder = os.path.join(dst_path_folder,currentMonth)
                os.makedirs(dst_path_folder, 0o666, exist_ok=True)
                dst_path = os.path.join(dst_path_folder,filename)                        

                #Check if same filename exists
                file_exists = os.path.isfile(dst_path)
                while file_exists:
                    #Log the duplicacy (v2.0)
                    
                    
                    #Rename the file by appending _copy
                    filename_split = filename.split(".")
                    filename = filename_split[len(filename_split)-2] + "_copy"
                    filename = filename + file_extension
                    dst_path = os.path.join(dst_path_folder,filename)
                    file_exists = os.path.isfile(dst_path)


                #Log the move (v2.0)

                #Move the file
                os.rename(file_path,dst_path)


            #Delete all empty folders
            for dir in dirs:
                dir_path = os.path.join(root, dir)

                #Log it for Deletion (v2.0)

                #Delete the folder
                os.rmdir(dir_path)
        return


class ChangedHandler(FileSystemEventHandler):

    def on_modified(self, event):
        #Destination Change Handler (v2.0)


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
    '.ini' : "Text/Other/System",
    '.lnk' : "Text/Other/System",
    '.msi' : "Text/Other/System",
    '.sys' : "Text/Other/System",
    '.tmp' : "Text/Other/System",
}

#Get current working directory
curr_dir = os.getcwd()

#Parse corresponding command line inputs
src_folder = args.src
dst_folder = args.dst
log_folder = args.log

#Create folders if they do not exist
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


#Create Source Looger - (v2.0)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
format_str = '%(asctime)s : %(created)f : %(funcName)s : %(message)s'
date_format = '%Y-%m-%D %H:%M:%S'
formatter = logging.Formatter(format_str,date_format)
source_log_file = log_folder + '/Source.log'
file_handler = logging.FileHandler(source_log_file)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#Create Destination Looger - (v2.0)
changed_logger = logging.getLogger(__name__)
changed_logger.setLevel(logging.DEBUG)
changed_log_file = log_folder + '/Category.log'
changed_file_handler = logging.FileHandler(changed_log_file)

#Create Source Observer
observer = Observer()
event = SourceHandler()
observer.schedule(event,src_folder,recursive=True)
observer.start()

#Create Destination Observer (v2.0)
changed_observer = Observer()
changed_event = ChangedHandler()
changed_observer.schedule(changed_event,dst_folder,recursive=True)
changed_observer.start()

#Start watching
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    #Stop watching
    observer.stop()
    changed_observer.stop()

#Join the observer threads
observer.join()
changed_observer.join()
