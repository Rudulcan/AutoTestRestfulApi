from backup_data_base import *
from restore_test_data_base import *
from service_handler import *
from restore_backup_data_base import *
import os
import sys


def main():
    cfg_parser = Parser()
    cfg_parser.set_attributes_from_config_file()

    output_to_file = ""
    if len(sys.argv) > 2:
        output_to_file = sys.argv[2]

    if len(sys.argv) > 1 and (sys.argv[1] == '--testCasesOnly' or sys.argv[1] == '--t'):
        prepare_outputfile()
        print("Running Tests!")
        run_tests(output_to_file)
    elif len(sys.argv) > 1 and (sys.argv[1] == '--complete' or sys.argv[1] == '--c'):
        service_name = cfg_parser.get_service_name()
        print("Stopping Service First")
        service_action("stop", service_name)
        print("Creating Backup!")
        create_backup_database()
        print("Creating DB to run the tests!")
        restore_test_database()
        print("Starting Service Now")
        service_action("start", service_name)
        prepare_outputfile()
        print("Running Tests!")
        run_tests(output_to_file)
        print("Stopping Service prior to start the restoring of the original database")
        service_action("stop", service_name)
        print("Restoring original Database after all the test cases have run")
        restore_backup_database()
        print("Starting Service Now")
        service_action("start", service_name)
    else:
        print("No Arguments!")
        print("Available arguments are:")
        print("--t, will run only testcases, you can also type --testCasesOnly")
        print("--c will stop the service, load DB amd run testcases, you can also type--complete")
        print("optionally you can send the results to an outputfile adding --o")
        print("e.g.:  python main.py --t --o")


def run_tests(output_to_file):
    count = len(Parser.list_of_files)
    for filename in Parser.list_of_files:
        if count > 0:
            if output_to_file == "--o":
                os.system('cmd /c "pytest -vv test_compare_request_response.py --filename "' + filename
                          + " >> " + Parser.get_test_output_filename() + " || type "
                          + Parser.get_test_output_filename())
            else:
                os.system('cmd /c "pytest -vv test_compare_request_response.py --filename "' + filename)
            count -= 1
        else:
            break


def prepare_outputfile():
    if path.exists(Parser.get_test_output_filename()):
        remove(Parser.get_test_output_filename())
    os.system('cmd /c "cls"')


if __name__ == "__main__":
    main()
