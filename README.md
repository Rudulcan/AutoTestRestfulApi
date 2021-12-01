# AutoTestRestfulApi
Python scripts to run automated tests on restful apis using pytest to compare expected results

##Prerequisites:
- A Restful api running as a service on a webserver such as Apache Tomcat 9
- MSSQL database working with the Restful Api

## Installation
These are python scripts so:

 - First, you need to install Python 3:  [Named Link](https://www.python.org/downloads/ "Python Download page")
 - ###Install Dependencies 
   - pip install pyodbc
   - pip install requests
   - pip install json
   - pip install pytest
   - pip install win32serviceutil
   
 - Get the code, and save it in a local folder such as C:\AutoTestRestFulApi
 - Configure the parameters of the RestFul Api by editing the file "test.cfg.xml" 
 - Create a Subfolder named "TestCases" e.g.: C:\AutoTestRestFulApi\TestCases
 - Create the testcases ypu want to run, every testFile must by saved in the TestCases folder


## How to Run 
* Open a CMD or terminal with administrative privileges (windows)/ root (linux)
* Call the main.py script like this:
  * python main.py --c
    
    --c will stop the service, load DB amd run testcases, you can also type--complete
    
  * Optionally you can run only the test cases like this:
  
    python main.py --t

