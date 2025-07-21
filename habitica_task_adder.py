# habitica_task_adder.py
"""
Template Script to Add a Habitica Task with a Checklist via the Habitica API.
Author: Martin Edwini-Bonsu
License: MIT
"""

import requests
import json
import os

# -----------------------------
# Load Habitica Credentials
# -----------------------------
USER_ID = os.getenv("HABITICA_USER_ID")
API_TOKEN = os.getenv("HABITICA_API_TOKEN")

if not USER_ID or not API_TOKEN:
    raise ValueError("Please set HABITICA_USER_ID and HABITICA_API_TOKEN as environment variables.")

API_URL = 'https://habitica.com/api/v3'

headers = {
    'x-api-user': USER_ID,
    'x-api-key': API_TOKEN,
    'Content-Type': 'application/json'
}

# -----------------------------
# Define Task Details Below
# -----------------------------
task = {
    "text": "Update my personal website",
    "type": "todo",
    "checklist": [
        {"text": "Add personal portfolio projects"},
        {"text": "Add headers to website"},
        {"text": "Add about me page"},
        # Add or modify checklist items as needed
    ]
}

# -----------------------------
# Send Task to Habitica API
# -----------------------------
def create_habitica_task(task_data):
    response = requests.post(f"{API_URL}/tasks/user", headers=headers, data=json.dumps(task_data))
    if response.status_code == 201:
        print(" Task created successfully!")
    else:
        print(f" Error {response.status_code}: {response.json()}")

if __name__ == "__main__":
    create_habitica_task(task)
