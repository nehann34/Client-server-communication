import socket

print("Hi,I'm client")
user= input("Please enter username:")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")

print("connecting to server.....")
s.connect(('192.168.43.50',6565))
print("Now you are connected to server,Start the communication.")
