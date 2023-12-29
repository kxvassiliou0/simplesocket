import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates the socket object
s.connect((socket.gethostname(), 2222)) # connect to the server's address and port

while True:
    msg = s.recv(1024) # receive data in chunks of 1024 bytes
    print(msg.decode("utf-8")) # decode the received bytes and print the message