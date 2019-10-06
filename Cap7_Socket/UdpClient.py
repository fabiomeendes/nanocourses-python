from socket import *

server = '127.0.0.1'
port = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server, port))
out = ''

while out != 'X':
    msg = input('Your message: ')
    obj_socket.sendto(msg.encode(), (server, port))
    data, source = obj_socket.recvfrom(65535)
    print('Server answer: ', data.decode())
    out = input('Type <X> to exit: ').upper()

obj_socket.close()
