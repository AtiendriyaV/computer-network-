import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()

client_socket.connect((host,1044))

num1=input("enter first number")

function = num1=int(input("enter first number"))
for i in range(1, 11):
 print(num1, 'x', i, '=', num1*i)
           
client_socket.send(f"{num1} {function}".encode())

result = client_socket.recv(1024).decode()

print(f"Result: {result}")

client_socket.close()
