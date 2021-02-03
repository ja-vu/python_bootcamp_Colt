import requests

url = "https://studio.cucumber.io/api/projects/119861/scenarios"
headers = {
    "Accept": "application/vnd.api+json; version=1",
    "access-token": "78YUZJXqz6y5ws-BRBEDaw",
    "client": "7Y-_9xuRrYBQhCMrmeUJpA",
    "uid": "hiptest@behavox.com"
}

res = requests.get(url, headers=headers,params="project_id")

print(res.json())
