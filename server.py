import socket

print("Server socket")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('192.168.43.50', 6565))

print("socket for accepting the connection",serversocket)
serversocket.listen(10)
(clientsocket, address) = serversocket.accept()
