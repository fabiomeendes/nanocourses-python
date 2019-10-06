import socket

ans = "S"

while ans == "S":
    url = input("Type a url: ")
    ip = socket.gethostbyname(url)
    print("IP:", ip)
    ans = input('Type "s" to continue: ').upper()