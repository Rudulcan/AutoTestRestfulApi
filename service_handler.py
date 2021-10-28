import win32serviceutil
import time

def service_running(service):
    return win32serviceutil.QueryServiceStatus(service)[1] == 4

def service_stopping(service):
    return win32serviceutil.QueryServiceStatus(service)[1] == 3


def service_action(action, service):
    running = service_running(service)

    if action.lower() == 'stop':
        if not running:
            print("Can not Stop: " + service + ", service is not running\n")
        else:
            win32serviceutil.StopService(service)
            stopping = service_stopping(service)
            print("Waiting for service " + service + " to stop")
            seconds = 0
            while stopping:
                print(".", end=' ', flush=True)
                time.sleep(1)
                stopping = service_stopping(service)
                seconds = seconds + 1

            print("Service " + service + " Stopped successfully after " + str(seconds) + " second(s)")


    if action.lower() == 'start':
        if running:
            print("Can not Start: " + service + ", service is already running\n")
        else:
            win32serviceutil.StartService(service)
            running = service_running(service)
            print("Waiting for service " + service + " to start")
            seconds = 0
            while not running:
                print(".", end=' ', flush=True)
                time.sleep(1)
                running = service_running(service)
                seconds = seconds + 1

            print("Service " + service + " Started successfully after " + str(seconds) + " second(s)")

