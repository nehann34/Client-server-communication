import socket
import threading
import queue

q_list=[]
q_list_lock=threading.Lock()

def rec_whole_size(sock, size):
	r = 0
	array = bytes()

	while r < size:
		array = array + sock.recv(size - r)
		r = len(array)
	return array

def send_to_client(my_q,client_sock):
    while True:
           
          message=my_q.get()
         # print("sending to client")
          client_sock.sendall(message)
          

def rec_from_client(my_q,client_sock):
    while True:
  
         message_size = rec_whole_size(client_sock, 3)
         int_message_size = int(message_size.decode('utf-8'))
         message = rec_whole_size(client_sock, int_message_size)
         print("Client",message.decode('utf-8'))
         with q_list_lock:
              for q in q_list:
                  if q is my_q:
                      pass
                  else :
                      q.put(message_size + message)
                     
    
print("Server socket")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('192.168.43.50', 6333))
print("socket for accepting the connection",serversocket)
serversocket.listen(10)

while True:
	sock, add = serversocket.accept()
	q = queue.Queue()
	with q_list_lock:
		q_list.append(q)

	tr = threading.Thread(target = rec_from_client, name = "receiving thread", args = [q, sock], daemon = True)
	ts = threading.Thread(target = send_to_client, name = "sending thread", args = [q, sock], daemon = True)	
	tr.start()
	ts.start()
