from http.server import BaseHTTPRequestHandler
from database import insert_data_into_database
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f"Received data: {post_data.decode('utf-8')}")

        # Сохранение данных в базу данных
        insert_data_into_database(post_data.decode('utf-8'))
            
        # Отправка ответа клиенту
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = {"status": "success"}
        self.wfile.write(json.dumps(response).encode('utf-8'))

        
    def log_message(self, format, *args):
        with open("server.log", "a") as f:
            f.write("%s - - [%s] %s\n" %
                     (self.address_string(),
                      self.log_date_time_string(),
                      format%args))