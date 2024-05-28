import psycopg2
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f"Received data: {post_data.decode('utf-8')}")

        # Сохранение данных в базу данных
        try:
            connection = psycopg2.connect(
                dbname="test_db",
                user="user1",
                password="user1",
                host="localhost"
            )
            cursor = connection.cursor()

            # Вставка данных в таблицу
            cursor.execute("INSERT INTO test_data (data) VALUES (%s)", (post_data.decode('utf-8'),))
            connection.commit()

            cursor.close()
            connection.close()
            
            # Отправка ответа клиенту
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {"status": "success"}
            self.wfile.write(json.dumps(response).encode('utf-8'))

        except psycopg2.Error as e:
            print("Error: Could not connect to the database.")
            print(e)
    
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
