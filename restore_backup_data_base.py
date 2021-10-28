import pyodbc
from test_parser import *


def restore_backup_database():
    pyodbc.pooling = False

    cfg_parser = Parser()
    cnxn = pyodbc.connect(cfg_parser.get_db_restore_connection_string())
    crsr = cnxn.cursor()
    cnxn.autocommit = True
    dbname = cfg_parser.get_db_name()
    full_path_restore_file_name = cfg_parser.get_backup_filepath() + cfg_parser.get_backup_filename()
    restore_data_full_file_path = cfg_parser.get_restore_data_full_file_path()
    restore_log_full_file_path = cfg_parser.get_restore_log_full_file_path()

    sql = "IF EXISTS (SELECT 0 FROM sys.databases WHERE name = '" + dbname + "') BEGIN USE master END"
    crsr.execute(sql)
    while (crsr.nextset()):
        pass
    sql = "IF EXISTS (SELECT 0 FROM sys.databases WHERE name = '" + dbname + "') BEGIN ALTER DATABASE " + dbname + " SET SINGLE_USER WITH ROLLBACK IMMEDIATE END"
    crsr.execute(sql)
    while (crsr.nextset()):
        pass

    sql = "IF EXISTS (SELECT 0 FROM sys.databases WHERE name = '" + dbname + "') BEGIN DROP DATABASE " + dbname + " END"
    crsr.execute(sql)
    while (crsr.nextset()):
        pass

    sql = "RESTORE DATABASE " + dbname + " FROM DISK = N'" + full_path_restore_file_name + "' WITH RECOVERY, MOVE N'" + dbname + "' TO N'" + restore_data_full_file_path + "', MOVE N'" + dbname + "_log' TO N'" + restore_log_full_file_path + "';"
    crsr.execute(sql)
    while (crsr.nextset()):
        pass

    sql = "IF EXISTS (SELECT 0 FROM sys.databases WHERE name = '" + dbname + "') BEGIN ALTER DATABASE ew SET MULTI_USER END"
    crsr.execute(sql)
    while (crsr.nextset()):
        pass
    crsr.close()
    cnxn.close()
