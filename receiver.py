import socket
import json
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))
client.send("I am CLIENT".encode())
from_server = client.recv(4096)
client.close()
dct = from_server.decode()
print(type(dct))
dct = json.loads(dct)
print(dct)
