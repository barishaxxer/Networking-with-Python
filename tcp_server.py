import socket

host = "localhost"
port = 1337

def main():

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server.bind((host, port))

	server.listen(5)
	# 5 is the number of clients that can connect
	mesg = 1
	while True:
		
		client, addr = server.accept()
		m_thread = threading.THREAD(target=handle_client, args=(client,addr,mesg))	
		m_thread.start()
		m += 1


def handle_client(client, addr, mesg):

	client.sendall(b"mesg")
	print("sending message")
	reply = sock.recv(4096)
	print("Succesfuly established")
	sock.send(b"ACK")

