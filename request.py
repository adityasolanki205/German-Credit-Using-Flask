import requests
import json

url = "http://localhost:5000/predict"
headers={"content-type": "application/json"}

# send HTTP request to the server
response = requests.post(url, data=open('X_test_json.json', 'rb'), headers=headers)
predictions = response.json()
print (predictions)
