import requests
import os
data = '{ "temperature": 10 }'
response = requests.post(os.environ['GATEWAY_URL'], data=data)
print(response.text)
