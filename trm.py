from sys import argv
from functions import log
from sqlite3 import *
from db_cmd import IS_DELETED
import os

db = connect("trm.sql", isolation_level=None)
cur = db.cursor()
files = [os.path.abspath(file) for file in argv[1:]]
files = log(files)

print(files)

for file in files:
    match file[1]:
        case "file":
            os.remove(file[0])
            cur.execute(IS_DELETED, [file[0]])
        case "dir":
            os.rmdir(file[0])
            cur.execute(IS_DELETED, [file[0]])
        case "link":
            os.unlink(file[0])
            cur.execute(IS_DELETED, [file[0]])

print(files)