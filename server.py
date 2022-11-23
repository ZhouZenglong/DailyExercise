from socket import*

IP = '127.0.0.1'
Port = 8888
Buflen = 512

listenSocket = socket(AF_INET,SOCK_STREAM)

listenSocket.bind((IP,Port))

listenSocket.listen(8)  
print(f'服务端启动成功，在｛Port｝端口等待客户连接...')

dataSocket,addr = listenSocket.accept()
print('接受一个客户端连接：',addr)

while True:
	recved = dataSocket.recv(Buflen)
	if not recved:
		break
	info = recved.decode()
	print(f'收到对方信息：{info}')

	dataSocket.send(f'服务端接受到了信息{info}'.encode())

dataSocket.close()
listenSocket.close()
