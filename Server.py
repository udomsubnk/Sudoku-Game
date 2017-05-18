import socket


def startServer(self):
      serversocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
      serversocket.bind((host,port))
      #queue up to n request
      serversocket.listen(10)
      print("SERVER START!")
      clientsocket,addr=serversocket.accept()
      print("CLIENT CONNECT ALREADY!")

def joinServer(self):
      s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
      host=' '
      port=9999
      #Connect to hostname on the part
      try:
            s.connect((host,port))
      except socket.error as msg:
            print (msg)
      
      
      
      
      
