import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('10.20.133.78',80))
cmd = 'GET http://10.20.133.78/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(521)
    if (len(data) <1):
        break
    print(data.decode(),end = '')
mysock.close()