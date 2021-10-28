import xml.etree.ElementTree as ET
import os


def get_response_for_test(file_name_path):
    cfg_file = "TestCases\\" + file_name_path
    response = ""

    tree = ET.parse(cfg_file)
    root = tree.getroot()

    for node in root.findall('property'):
        if node.attrib['name'] == "response":
            response = node.text

    return response


def get_request_for_test(file_name_path):
    cfg_file = "TestCases\\" + file_name_path
    request = ""

    tree = ET.parse(cfg_file)
    root = tree.getroot()

    for node in root.findall('property'):
        if node.attrib['name'] == "request":
            request = node.text

    return request


def get_type_request_for_test(file_name_path):
    cfg_file = "TestCases\\" + file_name_path
    request_type = ""

    tree = ET.parse(cfg_file)
    root = tree.getroot()

    for node in root.findall('property'):
        if node.attrib['name'] == "request.type":
            request_type = node.text

    return request_type


def get_header_request_for_test(file_name_path):
    cfg_file = "TestCases\\" + file_name_path
    request_header = ""

    tree = ET.parse(cfg_file)
    root = tree.getroot()

    for node in root.findall('property'):
        if node.attrib['name'] == "request.header":
            request_header = node.text

    return request_header


def get_method_request_for_test(file_name_path):
    cfg_file = "TestCases\\" + file_name_path
    request_header = ""

    tree = ET.parse(cfg_file)
    root = tree.getroot()

    for node in root.findall('property'):
        if node.attrib['name'] == "request.method":
            request_method = node.text

    return request_method


def get_params_request_for_test(file_name_path):
    cfg_file = "TestCases\\" + file_name_path
    request_params = ""

    tree = ET.parse(cfg_file)
    root = tree.getroot()

    for node in root.findall('property'):
        if node.attrib['name'] == "request.params":
            request_params = node.text

    return request_params


def traverse_files():
    path = "TestCases\\"
    for root, dirs, files in os.walk(path):
        for file in files:
            Parser.list_of_files.append(file)


class Parser:
    list_of_files = []
    service_name = None
    service_url = None
    driver = None
    server = None
    database = None
    uid = None
    pswd = None
    restorefilename = None
    restorefilepath = None
    restoredatafullfilepath = None
    restorelogfullfilepath = None
    backupfilename = None
    backupfilepath = None
    test_output_filename = None

    @staticmethod
    def set_attributes_from_config_file():
        tree = ET.parse('test.cfg.xml')
        root = tree.getroot()

        for node in root.findall('property'):
            if node.attrib['name'] == "service.url":
                Parser.service_url = node.text
            if node.attrib['name'] == "service.name":
                Parser.service_name = node.text
            if node.attrib['name'] == "driver":
                Parser.driver = node.text
            if node.attrib['name'] == "connection.serverName":
                Parser.server = node.text
            if node.attrib['name'] == "connection.database":
                Parser.database = node.text
            if node.attrib['name'] == "connection.username":
                Parser.uid = node.text
            if node.attrib['name'] == "connection.password":
                Parser.pswd = node.text
            if node.attrib['name'] == "restore.filename":
                Parser.restorefilename = node.text
            if node.attrib['name'] == "restore.filepath":
                Parser.restorefilepath = node.text
            if node.attrib['name'] == "restore.datafullfilepath":
                Parser.restoredatafullfilepath = node.text
            if node.attrib['name'] == "restore.logfullfilepath":
                Parser.restorelogfullfilepath = node.text
            if node.attrib['name'] == "backup.filename":
                Parser.backupfilename = node.text
            if node.attrib['name'] == "backup.filepath":
                Parser.backupfilepath = node.text
            if node.attrib['name'] == "testOutput.filename":
                Parser.test_output_filename = node.text
        traverse_files()

    @staticmethod
    def get_service_url():
        return Parser.service_url

    @staticmethod
    def get_service_name():
        return Parser.service_name

    @staticmethod
    def get_db_connection_string():
        conn_string = "DRIVER={" + Parser.driver + "}; SERVER=" + Parser.server + "; DATABASE=" + Parser.database + \
                      "; UID=" + Parser.uid + "; PWD=" + Parser.pswd + "; autocommit=True"
        return conn_string

    @staticmethod
    def get_db_restore_connection_string():
        conn_string = "DRIVER={" + Parser.driver + "}; SERVER=" + Parser.server + "; DATABASE=master; " \
                                                    "UID=" + Parser.uid + "; PWD=" + Parser.pswd + "; autocommit=True"
        return conn_string

    @staticmethod
    def get_db_name():
        return Parser.database

    @staticmethod
    def get_backup_filename():
        return Parser.backupfilename

    @staticmethod
    def get_backup_filepath():
        return Parser.backupfilepath

    @staticmethod
    def get_restore_filename():
        return Parser.restorefilename

    @staticmethod
    def get_restore_filepath():
        return Parser.restorefilepath

    @staticmethod
    def get_restore_data_full_file_path():
        return Parser.restoredatafullfilepath

    @staticmethod
    def get_restore_log_full_file_path():
        return Parser.restorelogfullfilepath

    @staticmethod
    def get_test_output_filename():
        return Parser.test_output_filename
