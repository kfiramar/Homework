import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))
Name = input("type your name: ")
Acc_PIN = input("type your code: ")
User = (Name + ":" + Acc_PIN)
client.send(User.encode('utf-8'))
from_server = client.recv(4096).decode('utf-8')
print(from_server)
if (from_server == "Denied"):
    client.close()
    SystemExit
print(client.recv(4096).decode('utf-8'))
withdraw = input()
client.send(withdraw.encode('utf-8'))
from_server = client.recv(4096).decode('utf-8')
print(from_server)


client.close()