#import socket
import socket

#get The Host name
hostname=socket.gethostname()

#get the IP Address
IP_Address=socket.gethostbyname(hostname)


print("Your IP Addresh is:",IP_Address)