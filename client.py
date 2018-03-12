import socket
import threading
def rec_whole_size(sock,size):
    r=0
    array= bytes()
    while r < size :
          array= array+ sock.recv(size-r)
          r=len(array)
    return array

def length_to_seven(size):
    size='0'*(7-len(size))+ size
    return size

#receive messages from server
def rec_msg_fromserver(server_sock):
    msg_size= int(rec_whole_size(server_sock, 7).decode("utf-8"))
    message = rec_whole_size(server_sock,msg_size)   
    if 'file: '.encode('utf-8') in message:
        p=message.strip('file: '.encode('utf-8'))
        file_to_write = open('xyz.txt', 'wb')
        file_to_write.write(p)
        file_to_write.close()
        print ('File received successfully')
    else:
        print(message)
      

print("Hi,I'm client")
username= input("Username:")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")
print("connecting to server.....")
s.connect(('192.168.43.50',48023))
print("Now you are connected to server,Start the communication.")

t = threading.Thread(target = rec_msg_fromserver, args=[s])
t.start()

while True :
      msg=input()
      
      if 'sending /' in msg:
          l1=[]
          l1=msg.split(' ')
          length=len(l1)
          m=l1[length-1]
          file_to_send = open(m, 'rb') 
          l = file_to_send.read()
          
          ap='file: '.encode('utf-8') + l
          size = length_to_seven(str(len(ap))).encode('utf-8')
          ap = size + ap
          s.sendall(ap)
          file_to_send.close()          
      
      else :
 
          message =username + ' sent : '+ msg
          size = length_to_seven(str(len(message)) )
          message = (size + message).encode("utf-8")
          s.sendall(message)
