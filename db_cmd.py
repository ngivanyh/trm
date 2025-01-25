LOG_DB = "INSERT INTO rm (filename, removed, rollback) VALUES (?, FALSE, FALSE)"
IS_DELETED = "UPDATE rm SET removed=TRUE WHERE filename=?"