import socket
import threading
def rec_whole_size(sock,size):
    r=0
    array= bytes()
    while r < size :
          array= array+ sock.recv(size-r)
          r=len(array)
    return array

def length_to_three(size):
    size='0'*(3-len(size))+ size
    return size

#receive messages from server
def rec_msg_fromserver(server_sock):
    msg_size= int(rec_whole_size(server_sock, 3).decode("utf-8"))
    message = rec_whole_size(server_sock,msg_size).decode("utf-8")
    print(message)    


print("Hi,I'm client")
username= input("Username:")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")
print("connecting to server.....")
s.connect(('192.168.43.50',6333))
print("Now you are connected to server,Start the communication.")

t = threading.Thread(target = rec_msg_fromserver, args=[s])
t.start()

while True :
      message =username + ' sent : '+input()
      size = length_to_three(str(len(message)) )
      message = (size + message).encode("utf-8")
      s.sendall(message)
