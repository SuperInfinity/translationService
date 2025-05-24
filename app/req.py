import json
import requests
import uuid

def send_req():
    url = "http://localhost:8000/events/"

    event_data = {
        "event_iddd": str(uuid.uuid4()),
        "event_type": "test_event",
        "event_data": {
            "msg": "AAAA!!!!",
        },
    }

    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post(url, data=json.dumps(event_data), headers=headers)

    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")
    print(f"Response Headers: {response.headers}")

if __name__ == '__main__':
    send_req()