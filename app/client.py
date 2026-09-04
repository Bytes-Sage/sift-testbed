"""HTTP client used throughout the app."""

import requests


def fetch_user(user_id: str) -> dict:
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()


def post_event(payload: dict) -> None:
    requests.post("https://api.example.com/events", json=payload, timeout=10)
