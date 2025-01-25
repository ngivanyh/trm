from sys import argv
from functions import *
import os

files = log([os.path.abspath(file) for file in argv[1:]])

for file in files:
    match file[1]:
        case "file":
            os.remove(file[0])
        case "dir":
            os.rmdir(file[0])
        case "link":
            os.unlink(file[0])
print(files)