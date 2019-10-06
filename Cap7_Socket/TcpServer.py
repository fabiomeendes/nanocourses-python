from socket import *

server = '127.0.0.1'  # localhost
port = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((server, port))
obj_socket.listen(2)

print('Waiting for client...')

while True:
    con, client = obj_socket.accept()
    print('Connecting with: ', client)
    while True:
        receivedMsg = str(con.recv(1024), 'utf-8')
        print('Received:', receivedMsg)
        sendMsg = b'Hello client'
        con.send(sendMsg)
        break
    con.close()
