import serial
from serial.tools import  list_ports

connection = ''

for port in list_ports.comports():
    print('Device: {} - port: {} '.format(port.description, port.device))
    if 'ARDUINO' in port.description.upper():
        try:
            connection = serial.Serial(port.device, 115200)
            print('Connection with {}.'.format(connection.portstr))
        except:
            pass

if connection != '':
    while True:
        answer = connection.readline()
        print(float(answer.decode()))
    connection.close()


# Arduino code

# void setup() {
#     Serial.begin(115200);
# }
#
# void loop() {
#     int light = analogRead(1); Analogic port of where is connected the arduino
#     Serial.println(light);
#     delay(1000); 1s
# }
