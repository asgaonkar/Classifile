# Classifile

> (Linux Based)

Categorically organise files according to date &amp and file type;

To make life easier and organised, it is highly imperative that we have our work placed structured.

## Version

> Classifile-1.0

## I/O

Input:  

> python3 Classifile.py [-h] -s SRC -d DST -l LOG

```
SRC: Source folder path (Dump)
DST: Destination directory path
LOG: Contains log files
```

Output: DST directory will be hierarchically structured based on Year, Month and file type.


> Mandatory switches: -s/--src, -d/--dst, -l/--log

> Optional Switches: -h

## Imports

> os, sys, time, fnmatch, logging, argparse, datetime, watchdog.observers, watchdog.events


## Example

Given below is an example using which it is easy to understand the working of Classifile

```
python3 Classifile.py -s Peronal/ -d Organised/ -l ../Logs/
```


## Vulnerability Checks
 > Vulnerability checks yet to be performed

## Coming Soon (v2.0)

Features to be included

```
Handling destination changes
Source Log
Destination Log
Optional sort using file creation/modified date
```

## Author

* **Atit S Gaonkar** - *Initial work* - [Github](https://github.com/asgaonkar) - [LinkedIN](https://www.linkedin.com/in/atit-gaonkar/)
