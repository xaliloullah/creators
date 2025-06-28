from utils.creator.src.commands import Command
from utils.creator.src.app.creator import Creator 
from utils.creator.src.servers.server import Server


class ServerCommand(Command):
    @classmethod
    def config(cls, subparsers):
        parser:Command = subparsers.add_parser('serve', help="Start a simple server")
        parser.add_argument('-p','--port', type=int, help="Port to run the server on")
        parser.add_argument('-d','--directory', help="Directory to serve files from (default: current working directory)")
        # parser.add_argument('-H', '--host', type=str, default='localhost', help="Host to run the server on (default: localhost)")
        # parser.add_argument('-b', '--bind', type=str, default='0.0.0.0', help="IP address to bind the server to (default: 0.0.0.0)")
        # parser.add_argument('--ssl', action='store_true', help="Enable SSL for the server")
        # parser.add_argument('--ssl-cert', type=str, help="Path to SSL certificate file")
        # parser.add_argument('--ssl-key', type=str, help="Path to SSL key file")
        # parser.add_argument('--ssl-ca', type=str, help="Path to SSL CA file")
        parser.set_defaults(func=cls.handle)
        

    @staticmethod
    def handle(args):
        """Start a server."""
        port = args.port
        if port:
            Server.set_port(port)
        # directory = args.directory or public_path('index.html')   
        # change_directory(directory)
        Server.start() 
        Creator.terminal.success(f"Server running on port: {Server.port}. URL: http://{Server.host}:{Server.port}")
        try:
            while not Server.stop_event.is_set():
                pass   
        except KeyboardInterrupt:
            Creator.terminal.warning(f"Stopping the server...")  
            Server.stop() 
