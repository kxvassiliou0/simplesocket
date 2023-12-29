# Simple Client-Server Socket Example
A very basic example of client-server communication, which forms the foundation for more complex digital interactions.

## Server Script
  * Creates a socket object for communication.
  * Binds the socket to the local machine's hostname and port 2222.
  * Listens for incoming connections and establishes a connection when a client connects.
  * Prints a connection message and sends a welcome message to the client.

## Client Script
  * Creates a socket object for communication.
  * Connects to the server's hostname and port 2222.
  * Enters into a loop to continuously receive data from the server.
  * Prints the received message after decoding it from bytes using UTF-8.

## Communication Flow
  1. The server script binds to a specific address and port, listens for incoming connections, and accepts connections from clients.
  2. The client script connects to the server's address and port.
  3. Once a connection is established, the server sends a welcome message to the client.
  4. The client receives and prints the welcome message.

![CMD SS](https://github.com/kxvassiliou0/simplesocket/assets/34982747/48949691-cb01-4ded-a71f-a7a36aa2fa06)
*The above image shows the client-server interaction in command-prompt windows, side-by-side.*
