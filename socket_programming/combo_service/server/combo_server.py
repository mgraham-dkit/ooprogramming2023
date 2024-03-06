import socket
import combo_service


def handle_client(conn, addr):
    session = True
    while session:
        request = conn.recv(1024)
        if request:
            # Logic for protocol
            pass
        else:
            session = False


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((combo_service.HOST, combo_service.PORT))
    server_socket.listen()
    while True:
        conn, addr = server_socket.accept()
        handle_client(conn, addr)
        print(f"Connection to {addr} closed")