import socket

def client_program():
      host= socket.gethostname()
      port= 5000
      client_socket = socket.socket()
      client_socket.connect((host,port))
      massage = ("->")
      print("Connedted...")
      while message.lower().strip()!= 'bye':
            client_socket.send(massage.encode())
            data= client_socket.rev(1024).decode()
            print("Recived from sender")
      Client_socket.close()

if __name__ == ' __main__ ':
      client_program()

