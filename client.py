
import requests

url = "http://127.0.0.1:8000/"
headers = {
    "Content-Type": "application/json"
}

while True:
    x = input("input your question: ")

    data = {
        "payload": x
    }

    response = requests.post(url, json=data, headers=headers)

    print(response.status_code)
    print(response.json()["messages"][-1])  # or response.text

    print("\n\n\n\n")
