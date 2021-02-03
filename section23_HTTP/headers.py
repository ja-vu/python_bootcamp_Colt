import requests

url = "https://icanhazdadjoke.com/"

# response = requests.get(url, headers={"Accept":"text/plain"})
response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()

print(data)
print(data['joke'])
print(f"status: {data['id']}")

# Query string
# - A way to pass data to the server as part of a GET request
# http://www.example/?key1=value1&key2=value2
