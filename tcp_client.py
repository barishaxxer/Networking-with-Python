import socket

host = "barishaxxer.github.io"
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET6 -> ipv6
# SOCK.DGRAM -> udp

client.connect((host, port))

client.send(b'GET / HTTP/1.1\r\nHost: barishaxxer.github.io\r\n\r\n')
# because of https conventions we need \r\n and no gaps between
print(client.recv(4096).decode())


