import os,sys
from socket import *
class TcpClient:
    HOST='127.0.0.1'
    PORT=1122
    BUFSIZ=2048
    ADDR=(HOST, PORT)
    def __init__(self):
        self.client=socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.ADDR)
        while True:
            information=input('Shell >>')
            if not information:
                break
            self.client.send(information.encode('utf8'))
            if information.upper()=="QUIT":
                break
            information=self.client.recv(self.BUFSIZ)
            if not information:
                break
            print('cmd：%s' %(information.decode('utf8')))
if __name__ == '__main__':
    client=TcpClient()