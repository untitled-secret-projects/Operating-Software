

# encode() must always be used when writing as unicode strings are not supported in serial.


import serial

class Cellular:

    # cellular attributes
    port = '/dev/serial0'
    rate = 115200

    # initialises the serial connection
    def __init__(self):
        print('initialising serial connection')
        self.cellularSerial = serial.Serial(Cellular.port, Cellular.rate, timeout=0.5)
        response = self.cellularSerial.readlines(None)

        # Switching off echo of Hayes key commands
        self.cellularSerial.write("ATE0\r".encode())
        response = self.cellularSerial.readlines(None)
        self.cellularSerial.write("AT\r".encode())
        response = self.cellularSerial.readlines(None)
        print(response)

    def getCommand(self):
        command = input("Enter your command [call, hang, answer, end]:\n")
        return command
    
    def dial_number(self):
        number = input("Enter the number to call:\n")
        self.cellularSerial.write(('ATD+65' + str(number) + ';\r').encode())
        response = self.cellularSerial.readlines(None)
        print(response)
    
    def hang_up(self):
        print("Hanging up...\n")
        self.cellularSerial.write(('AT+CHUP\r').encode())
        response = self.cellularSerial.readlines(None)
        print(response)

    def answer_call(self):
        print("Answering call...\n")
        self.cellularSerial('ATA\r'.encode())
        response = self.cellularSerial.readlines(None)
        print(response)
    

connection = Cellular()

while True:
    command = connection.getCommand()
    if (command == 'exit'):
        break
    if (command != 'call' and command != 'hang' and command != 'answer'):
        print("wrong command")
        continue
    
    if (command == 'call'):
        connection.dial_number()
    
    if (command == 'hang'):
        connection.hang_up()
    
    if (command == 'answer'):
        connection.answer_call()
    



    


        
