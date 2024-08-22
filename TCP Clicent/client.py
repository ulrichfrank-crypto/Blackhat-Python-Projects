import socket

target_host = 'zenithbank.com'
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#create a connection
client.connect((target_host, target_port))

#send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#recieve data response
response = client.recv(4096)

#print response
print (response)