import requests
from config.api_config import BASE_URL


def get(endpoint):
    r = requests.get(f"{BASE_URL}/{endpoint}")
    return r.json()


def post(endpoint, data):
    return requests.post(f"{BASE_URL}/{endpoint}", json=data)


def put(endpoint, data):
    return requests.put(f"{BASE_URL}/{endpoint}", json=data)


def delete(endpoint):
    r = requests.delete(f"{BASE_URL}/{endpoint}")
    return r