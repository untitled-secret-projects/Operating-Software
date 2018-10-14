import time
import pexpect
import subprocess
import sys

class BluetoothctlError(Exception):
    """
    This exception is raised, when bluetoothctl fails to start.
    """
    pass

class Bluetoothctl:
    '''
    A wrapper for bluetoothctl utility.
    '''

    # Constructor
    def __init__(self):
        # to make sure bluetooth is working.
        out = subprocess.check_output("rfkill unblock bluetooth", shell = True)
        
        # create a object attribute called child.
        self.child = pexpect.spawn("bluetoothctl", echo = False)

    # run a command in bluetoothctl prompt, return output as a list of lines.
    def get_output(self, command, pause = 0):
        self.child.send(command + "\n")
        time.sleep(pause)
        # pexpect is passed in as a predefined constant. This reads up to the EOF without generating an exception by using the EOF patetern expect
        start_failed self.child.expect(["bluetooth", pexpect.EOF])

        if start_failed:
            raise BluetoothctlError("Bluetoothctl failed after running " + command)

        return self.child.before.split("\r\n")


    def get_command():
        command = input("What's the command for bluetooth?")
        
