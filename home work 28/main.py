import socket


def create_chat_server(host, port):
    global server_socket
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Chat server is listening on {host}:{port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")
            handle_client(client_socket)

    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    finally:
        server_socket.close()


def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
            # Process the data or save it to a file here
    except ConnectionResetError:
        print("Client disconnected.")
    finally:
        client_socket.close()


if __name__ == "__main__":
    host = "127.0.0.1"  # Localhost
    port = 12345  # Choose any available port
    create_chat_server(host, port)
