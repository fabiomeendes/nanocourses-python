# pyserial
import serial
from serial.tools import list_ports

# list the arduino ports
for port in list_ports.comports():  # communication ports
    print('Device: {} - port: {} '.format(port.description, port.device))

connection = serial.Serial('COM3', 115200)  # Windowns, Linux - /dev/ttyUSB0 (SO port)
# see the arduino port, where he is plugged in

action = input('Type:\n<L> to turn ON\n<D> para turn OFF').upper()
while action == 'L' or action == 'D':
    if action == 'L':
        connection.write(b'1')
    else:
        connection.write(b'0')
    action = input('Type:\n<L> to turn ON\n<D> para turn off').upper()

connection.close()
print('Connection closed')


# Arduino code

# void setup() {
#     pinMode(10, OUTPUT);
#     Serial.begin(115200);
# }
#
# void loop() {
#     int receivedValue;
#     if (Serial.available()) {
#         receivedValue  = Serial.read();
#         if (receivedValue == '0') {
#             digitalWrite(10, LOW);
#         } else {
#             digitalWrite(10, HIGH);
#         }
#     }
# }




