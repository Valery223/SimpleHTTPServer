import requests
import json

url = 'http://localhost:8080'
data = {'message': 'Hello, server!'}

response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

print(f"Response from server: {response.text}")