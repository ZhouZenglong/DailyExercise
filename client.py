from socket import*

IP = '127.0.0.1'
SERVER_PORT = 8888
Buflen = 1024

dataSocket = socket(AF_INET,SOCK_STREAM)

dataSocket.connect((IP,SERVER_PORT))

while True:
	toSend =input('>>> ')
	if  toSend == 'exit':
		break
	dataSocket.send(toSend.encode())
	recved = dataSocket.recv(Buflen)
	if not recved:
		break
	print(recved.decode())

dataSocket.close()