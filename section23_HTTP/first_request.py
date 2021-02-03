# 1. DNS Lookup
# 2. Computer makes a REQUEST to a server
# 3. Server processes the RESPONSE
# 4. Server issues a RESPONSE

import requests

url = "http://google.com"
response = requests.get(url)

print(f"your request to {url} came back with status code {response.status_code}")
