import pyodbc
from test_parser import *
from os import path, remove


def create_backup_database():
    pyodbc.pooling = False
    cfg_parser = Parser()
    cnxn = pyodbc.connect(cfg_parser.get_db_connection_string())
    crsr = cnxn.cursor()
    dbname = cfg_parser.get_db_name()
    backup_file_name = cfg_parser.get_backup_filename()
    full_path_backup_file_name = cfg_parser.get_backup_filepath() + cfg_parser.get_backup_filename()
    if path.exists(full_path_backup_file_name):
        remove(full_path_backup_file_name)

    cnxn.autocommit = True
    crsr.execute(
        r"BACKUP DATABASE [" + dbname + "] TO  DISK = N'" + full_path_backup_file_name + "' WITH NOFORMAT, NOINIT,  NAME = N'" + backup_file_name + "', SKIP, NOREWIND, NOUNLOAD,  STATS = 10"
    )
    while (crsr.nextset()):
        pass
    crsr.commit()
    crsr.close()
    cnxn.autocommit = False
    cnxn.close()
    del cnxn
