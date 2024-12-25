import socket
import threading

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
		m_thread = threading.Thread(target=handle_client, args=(client,addr,mesg))	
		m_thread.start()
		mesg += 1


def handle_client(client, addr, mesg):

	client.sendall(f"message {mesg} ".encode())
	print("sending message")
	reply = client.recv(4096)
	print("Succesfuly established")
	print(reply.decode())
	client.send(b"ACK")


if __name__ == "__main__":
	main()
