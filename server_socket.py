# Server in Python using sockets library
# Server uses sockets to recieve incoming connections and provide with data, opposite of the Client
# Server --> Open socket, bind to an addr, listen for incoming connections, accept connections, read/send
#

import socket
import sys

HOST = '' #Simply implies allow any host connection
PORT = 8000 #Arbitrary 4 digit number, avoiding using the smaller ports which are designated for system use

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind the specified port to the socket, capture all incoming data
try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error: ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
    
print 'Socket bind complete'

#listen for any incoming connections over this port, 10 means only 10 connections are allowed to be waiting
s.listen(10)
print 'Socket now listening'

conn, addr = s.accept()

#display client information
print 'Connected with ' + addr[0] + ':' + str(addr[1])

#Now send information to the client
data = conn.recv(1024)
conn.sendall(data)

conn.close()
s.close()