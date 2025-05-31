import socket
import threading

class Server:
    port = 8000
    host = "localhost"
    listen = 50
    stop_event = threading.Event()

    @classmethod
    def run(cls): 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((cls.host, cls.port))
            server_socket.listen(cls.listen)    

            while not cls.stop_event.is_set():
                try: 
                    server_socket.settimeout(1.0) 
                    try:
                        client_socket, address = server_socket.accept()
                        print(f"Connexion acceptée depuis : {address}") 
                        threading.Thread(target=cls.handle_client, args=(client_socket, address), daemon=True).start()
                    except socket.timeout:
                        continue
                except Exception as e:
                    print(f"Erreur du serveur : {e}")
                    break

    @staticmethod
    def handle_client(client_socket, address):
        with client_socket:
            print(f"Gestion du client : {address}")
            while True:
                try:
                    # Recevoir des données du client
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    print(f"Message reçu de {address} : {data.decode()}")
                    # Répondre au client
                    client_socket.sendall("Message reçu !")
                except Exception as e:
                    print(f"Erreur avec le client {address} : {e}")
                    break

    @classmethod
    def get_port(cls):
        return cls.port

    @classmethod
    def set_port(cls, port):
        cls.port = port

    @classmethod
    def get_host(cls):
        return cls.host

    @classmethod
    def set_host(cls, host):
        cls.host = host

    @classmethod
    def start(cls):
        server_thread = threading.Thread(target=cls.run, daemon=True)
        server_thread.start()

    @classmethod
    def stop(cls):
        cls.stop_event.set()
