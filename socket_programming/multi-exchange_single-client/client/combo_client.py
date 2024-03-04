# Import socket module
import socket


# Define address information - IP AND port
HOST = "localhost"
PORT = 7878

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Request/make a connection : CLIENT LOGIC
    client_socket.connect((HOST, PORT))

    # Option B
    session = True
    while session:
        # Exchanging information:
        # Logical conditions for start/stop
        #   sending a message
        msg = input("Please enter the message to be sent (-1 to end): ")
        if msg != "-1":
            client_socket.sendall(bytes(msg, 'utf-8'))
            #   receiving a message
            response = client_socket.recv(1024)

            print(f"Message received: {response.decode('utf-8')}")
        else:
            session = False

print("Connection terminated")

