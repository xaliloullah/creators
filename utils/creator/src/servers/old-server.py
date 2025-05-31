import socketserver
import threading
import os
from urllib.parse import parse_qs, urlparse
import json
import cgi

class Server:
    port = 8000
    host = "localhost" 
    stop_event = threading.Event()
    
    class Handler(socketserver.BaseRequestHandler):
        
        # def handle(self): 
        #     data = self.request.recv(1024).decode('utf-8')
        #     # print(f"Received from {self.client_address}:\n{data}")
            
        #     handle = self.handle_request(data)
             
        #     print("Method:", handle.get("method"))
        #     print("Path:", handle.get("path"))
        #     print("Headers:", handle.get("headers"))
        #     print("Body:", handle.get("body"))
        
        #     head= {}
        #     response = Response(format='json') 
        #     response.set_status_code(200)
        #     response.set_body("<html><body><h1>Hello, World!</h1></body></html>") 
        #     for key, value in handle.get("headers").items():
        #         # response.set_header(key, value)
        #         head[key] = value
                
        #     print(head)
                 
                 
        #     self.request.sendall(response.send().encode('utf-8'))
            
        # def handle_request(self, data): 
        #     lines = data.split("\r\n")
        #     request_line = lines[0].split(" ")
        #     method = request_line[0]
        #     path = request_line[1]
        #     headers = {}
        #     body = ""
        #     separator_index = lines.index('')   
        #     for line in lines[1:separator_index]:
        #         if ": " in line:
        #             key, value = line.split(": ", 1)
        #             headers[key] = value 
        #     body = "\r\n".join(lines[separator_index+1:])
            
        #     return {
        #         'method':method,
        #         'path':path,
        #         'headers':headers,
        #         'body':body
        #     }
        
        def handle(self):
            # Réception de la requête
            request_data = self.request.recv(2048).decode('utf-8')
            print("Requête reçue:")
            print(request_data)

            # Découper la ligne de la requête (méthode, chemin, version)
            request_line = request_data.split("\r\n")[0]
            method, path, version = request_line.split(" ")

            print(f"Méthode: {method}")
            print(f"Chemin: {path}")
            print(f"Version: {version}")

            # Extraction des paramètres GET (si présents)
            url_parts = urlparse(path)
            query_params = parse_qs(url_parts.query)
            print(f"Paramètres GET (URL): {query_params}")

            # Séparer les en-têtes de la requête
            headers = {}
            for line in request_data.split("\r\n")[1:]:
                if line == "":
                    break  # Fin des en-têtes
                key, value = line.split(":", 1)
                headers[key.strip()] = value.strip()

            print("En-têtes:")
            for key, value in headers.items():
                print(f"{key}: {value}")

            # Extraction des cookies (si présents)
            cookies = {}
            if 'Cookie' in headers:
                cookie_header = headers['Cookie']
                cookies = {cookie.split('=')[0].strip(): cookie.split('=')[1].strip() for cookie in cookie_header.split(';')}
            print("Cookies:")
            print(cookies)

            # Corps de la requête (si présent)
            body = ""
            if "Content-Length" in headers:
                content_length = int(headers["Content-Length"])
                body = request_data.split("\r\n\r\n", 1)[1][:content_length]
                print("Corps de la requête:")
                print(body)

            # Traitement des données selon le type de contenu
            if "Content-Type" in headers:
                content_type = headers["Content-Type"]
                if "application/x-www-form-urlencoded" in content_type:
                    parsed_data = parse_qs(body)
                    print("Paramètres du formulaire (x-www-form-urlencoded):")
                    for key, value in parsed_data.items():
                        print(f"{key}: {value}")
                elif "application/json" in content_type:
                    try:
                        parsed_json = json.loads(body)
                        print("Données JSON reçues:")
                        print(parsed_json)
                    except json.JSONDecodeError:
                        print("Erreur de décodage JSON.")
                elif "multipart/form-data" in content_type:
                    # Décodage des fichiers et des champs de formulaire multipart
                    _, params = cgi.parse_header(content_type)
                    boundary = params['boundary'].encode()
                    fields = self.parse_multipart_form_data(body, boundary)
                    print("Données multipart (formulaires et fichiers):")
                    for field in fields:
                        print(field)
                else:
                    print(f"Type de contenu non supporté: {content_type}")
            
            # Réponse HTTP
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nRéponse du serveur"
            self.request.sendall(response.encode('utf-8'))

        def parse_multipart_form_data(self, body, boundary):
            # Fonction pour décoder les données multipart/form-data
            fields = []
            parts = body.split(boundary)[1:-1]
            for part in parts:
                headers, content = part.split("\r\n\r\n", 1)
                content = content.rstrip("\r\n--")
                content_type = None
                for line in headers.split("\r\n"):
                    if line.startswith("Content-Disposition:"):
                        disposition = line.split("Content-Disposition: ")[1]
                        if 'filename' in disposition:
                            content_type = 'file'
                        else:
                            field_name = disposition.split("name=")[1].strip('"')
                            fields.append((field_name, content))
                if content_type != 'file':
                    fields.append((field_name, content))
            return fields

    @classmethod
    def run(cls): 
        server = socketserver.TCPServer((cls.host, cls.port), cls.Handler) 
        
        try: 
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally: 
            server.shutdown()
            server.server_close() 
    
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



class Response:
    def __init__(self, format='html'):
        self.headers = {}
        self.body = ""
        self.status_code = 200
        self.format = format  

    def set_header(self, key, value):
        """Set a specific header in the response."""
        self.headers[key] = value

    def get_header(self, key):
        """Retrieve the value of a specific header."""
        return self.headers.get(key)

    def set_body(self, body):
        """Set the body content of the response."""
        self.body = body

    def append_body(self, content):
        """Append content to the body of the response."""
        self.body += content

    def set_status_code(self, status_code):
        """Set the HTTP status code for the response."""
        self.status_code = status_code

    def set_format(self, format):
        """Set the response format (either 'html' or 'json')."""
        self.format = format

    def send(self):
        """Convert the response into an HTTP response string."""
        status_line = f"HTTP/1.1 {self.status_code} {self._get_status_message()}"
        headers = "\r\n".join(f"{key}: {value}" for key, value in self.headers.items())
        
        # Adjust body formatting based on the response format
        if self.format == 'json':
            import json

            self.headers['Content-Type'] = 'application/json'
            try:
                body = json.dumps(self.body)  # Encode la réponse JSON
            except (TypeError, ValueError) as e:
                body = json.dumps({"error": "Invalid JSON body", "details": str(e)})
                self.status_code = 500 
                
        elif self.format == 'html':  # default to HTML
            self.headers['Content-Type'] = 'text/html'
            body = self.body
        else:
            self.headers['Content-Type'] = 'text/plain'
            body = self.body
        
        return f"{status_line}\r\n{headers}\r\n\r\n{body}"

    def _get_status_message(self):
        """Retrieve a standard message for the current status code."""
        status_messages = {
            200: "OK",
            201: "Created",
            204: "No Content",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            500: "Internal Server Error",
            502: "Bad Gateway",
            503: "Service Unavailable",
        }
        return status_messages.get(self.status_code, "Unknown Status")
