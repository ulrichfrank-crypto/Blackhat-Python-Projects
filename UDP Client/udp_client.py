import socket

#define variables and assign values
target_host = '127.0.0.1'  # The server's hostname or IP address
target_port = 80  # The port used by the server

#creating a data object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto(b"Creating my first udp client",(target_host,target_port))

#recieve some data
data, addr = client.recvfrom(4096)

#print data
print(data)