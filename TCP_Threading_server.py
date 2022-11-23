from socket import *
import time, threading

s = socket(AF_INET,SOCK_STREAM)

s.bind(("",5001))

s.listen(5)

thread_list = []

def client_commu(client_socket):
	data = client_socket.recv(1024)
	print("Received:%s" % data.decode('ascii'))
	timestr = time.ctime(time.time())+"\r\n"

	client_socket.send(timestr.encode('ascii'))
	client_socket.close()

while True:
	ns,addr = s.accept()
	print("Got a connection from %s" % str(addr))

	t = threading.Thread(target = client_commu,args = (ns,))
	t.daemon = True
	thread_list.append(t)
	t.start()