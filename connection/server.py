import socket
def server_program():
      host = socket.gethostname()
      port = 5000      
      server_socket = socket.socket()
      server_socket.bind((host,port))
      server_socket.listen(1)
      print("Connection From:" +str(address))
      while True:
            data + Conn.recv(1024).decode()
            if not data:
                  break
            print("From Connected User:" + str(data))
            data = input("->")
            conn.send(data.encode)
      conn.close()
if __name__ == "__ main __":
      server_program()
print("Has connected the client")
