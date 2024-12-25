import socket

host = "localhost"
port = 1337

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"ELITE", (host, port))

data, addr = client.recvfrom(4096)
#addr is the address data is coming from
#take 4096 bytes

print(data.decode())
