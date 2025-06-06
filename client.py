
import requests

url = "your url"
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
    print(response.json()["messages"][-1]["content"])  # or response.text

    print()
