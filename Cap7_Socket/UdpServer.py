from socket import *

server = '127.0.0.1'
port = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((server, port))
print('Server ready!')

while True:
    data, source = obj_socket.recvfrom(65535)
    print('Source.........:', source)
    print('Received data..:', data.decode())
    answer = input('Type the answer: ')
    obj_socket.sendto(answer.encode(), source)

obj_socket.close()