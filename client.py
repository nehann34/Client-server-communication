import socket

def rec_whole_size(sock,size):
    r=0
    array= bytes()
    while r < size :
          array= array+ sock.recv(size-r)
          r=len(array)
    return array

def length_to_three(size)
    size='0'*(3-len(size))+ size
    return size


print("Hi,I'm client")
user= input("Please enter username:")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")

print("connecting to server.....")
s.connect(('192.168.43.50',6565))
print("Now you are connected to server,Start the communication.")
