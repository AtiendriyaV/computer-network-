import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
host = socket.gethostname()

server_socket.bind((host, 1044))

server_socket.listen(2)
print('Server ready to receive...')
while True:

  client_socket, addr = server_socket.accept()
print(f'Connected by {addr}')
data = client_socket.recv(1024).decode()
 
num1= data.split()
 
result = 'Invalid operator'

client_socket.send(str(result).encode())

client_socket.close()
