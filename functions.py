import os
from sqlite3 import *
from db_cmd import LOG_DB

def log(fileList: list):
    db = connect("trm.sql", isolation_level=None)
    cur = db.cursor()
    res = []
    print(os.path.isfile(fileList[0]))
    for file in fileList:
        if os.path.isfile(file):
            print("file")
            res.append([file, "file"])
            cur.execute(LOG_DB, [file])
        elif os.path.isdir(file):
            print("dir")
            res.append([file, "dir"])
            cur.execute(LOG_DB, [file])
        elif os.path.islink(file):
            print("link")
            res.append([file, "link"])
            cur.execute(LOG_DB, [file])
    return res