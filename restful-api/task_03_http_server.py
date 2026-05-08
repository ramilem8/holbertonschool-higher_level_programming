from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):

    
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode())

  
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.wfile.write(json.dumps(data).encode())

        
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write("OK".encode())

       
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.wfile.write(json.dumps(info).encode())

        
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write("Endpoint not found".encode())


HOST = "localhost"
PORT = 8000

server = HTTPServer((HOST, PORT), SimpleAPIHandler)

print(f"Server running on http://{HOST}:{PORT}")

server.serve_forever()