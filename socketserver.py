import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates the socket object
s.bind((socket.gethostname(), 2222)) # binding the socket to a specific address and port
s.listen(5) # listening for incoming connections, queue up to 5 clients

while True:
    clientsocket, address = s.accept() # accepting a connection
    print(f"Connection from {address} has been established!") # visual feedback, confirming a connection
    clientsocket.send(bytes("Welcome to the server", "utf-8")) # sending a welcome message