from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_lenght = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_lenght)
        
        print(f"Received data: {post_data.decode('utf-8')}")

        data = json.loads(post_data)
        processed_data = {"status": "processed", "original_data": data}
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(processed_data).encode('utf-8'))
    
    def log_message(self, format, *args):
        with open("server.log", "a") as f:
            f.write("%s - - [%s] %s\n" %
                     (self.address_string(),
                      self.log_date_time_string(),
                      format%args))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
