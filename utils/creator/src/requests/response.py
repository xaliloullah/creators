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

    def to_http_response(self):
        """Convert the response into an HTTP response string."""
        status_line = f"HTTP/1.1 {self.status_code} {self._get_status_message()}"
        headers = "\r\n".join(f"{key}: {value}" for key, value in self.headers.items())
        
        # Adjust body formatting based on the response format
        if self.format == 'json':
            self.headers['Content-Type'] = 'application/json'
            # Ensure the body is valid JSON, for simplicity, wrap it as a JSON object
            body = f"{{\"data\": \"{self.body}\"}}"
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
