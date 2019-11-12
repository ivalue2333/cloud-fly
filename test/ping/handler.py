import requests

if __name__ == "__main__":
    # requests.get("http://127.0.0.1:5000/api/v1/ping", data={"name": "你好"})
    requests.get("http://127.0.0.1:5000/api/v1/ping?age=10", json={"name": "你好"})
