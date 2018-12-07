import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 2600

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip,bind_port))

# This funtion displays what is received from the client and responds
def handle_client(client_socket):

    # Display data from client
    request = client_socket.recv(1024)

    print("[*] Received: %s" % request)

    # Send back an ACK!
    client_socket.send(b"ACK!")

    client_socket.close()


while True:

    client,addr = server.accept()

    print("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))

    # Create and start variable to handle data from the client
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()

