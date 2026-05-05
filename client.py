import requests

url = "http://127.0.0.1:8000/hello"

response = requests.post(url)

print("Статус:", response.status_code)
print("Відповідь:", response.json())
