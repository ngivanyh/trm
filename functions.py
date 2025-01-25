import os
from sqlite3 import *
from db_cmd import LOG_DB

def log(fileList: list):
    db = connect("trm.sql")
    cur = db.cursor()
    res = []
    for file in fileList:
        if os.path.isfile(file):
            res.append([file, "file"])
            cur.execute(LOG_DB, [file])
        elif os.path.isdir(file):
            res.append([file, "dir"])
            cur.execute(LOG_DB, [file])
        elif os.path.islink(file):
            res.append([file, "link"])
            cur.execute(LOG_DB, [file])
    return res