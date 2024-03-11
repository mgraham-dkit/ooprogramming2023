import socket
import combo_service
import datetime

def handle_client(conn, addr):
    session = True
    while session:
        request = conn.recv(1024).decode('utf-8')
        if request:
            # Logic for protocol
            components = request.split(combo_service.DELIMITER)
            global message_count
            message_count += 1
            match components[0]:
                case combo_service.ECHO:
                    response = components[1]
                case combo_service.DAYTIME:
                    response = datetime.datetime.now().__str__()
                case combo_service.STATS:
                    response = f"{message_count}"
                case _:
                    response = combo_service.INVALID

            conn.sendall(bytes(response, 'utf-8'))
        else:
            session = False


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((combo_service.HOST, combo_service.PORT))
    server_socket.listen()
    message_count = 0
    while True:
        conn, addr = server_socket.accept()
        handle_client(conn, addr)
        print(f"Connection to {addr} closed")