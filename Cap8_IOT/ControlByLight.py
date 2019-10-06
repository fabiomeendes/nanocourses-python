import serial
from serial.tools import list_ports

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
    print('Begin....')
    while True:
        print('Receiving data...')
        answer = connection.readline()
        value = float(answer.decode())
        print(value)
        if value < 700:
            connection.write(b'1')
        else:
            connection.write(b'0')

    connection.close()
    print('Connection closed')
else:
    print('Without available ports')

# Arduino code

# void setup() {
#     pinMode(10, OUTPUT); // LED
#     Serial.begin(115200); // Transfer tax
# }

# void loop() {
#     int receivedValue;
#     int light = analogRead(1);
#     Serial.println(light);
#     delay(500);
#     receivedValue = Serial.read();
#   if (receivedValue == '0') {
#       digitalWrite(10, LOW);
#   } else {
#       digitalWrite(10, HIGH);
#   }
# }
