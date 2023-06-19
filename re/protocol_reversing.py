
import socket
import struct

def protocol_reversing(target_ip, target_port):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the target
    s.connect((target_ip, target_port))

    # Receive the initial message
    msg = s.recv(1024)

    # Print the received message
    print('Received:', msg)

    # Send a message to the target
    s.sendall(b'Hello, server')

    # Receive the response
    data = s.recv(1024)

    # Print the response
    print('Received:', data)

    # Close the connection
    s.close()

if __name__ == "__main__":
    target_ip = "192.168.1.1"
    target_port = 80
    protocol_reversing(target_ip, target_port)
