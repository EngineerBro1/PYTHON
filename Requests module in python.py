# The requests module in Python is a popular HTTP library that allows you to send HTTP requests easily and handle responses. It provides a more user-friendly alternative to Python's built-in urllib.request module.


# Get Request:
import requests
response = requests.get("https://api.example.com/data")

if response.status_code == 200:
    print(response.text)
else:
    print("Error",response.status_code)


# Passing Parameter:
import requests
response = requests.get("https://api.example.com/search",params={"q":"python"})
print(response.text)


# Post:
import requests
response = requests.post("https://api.example.com/submit",data={"key":"value"})
print(response.text)


# Json :
import requests
response = requests.get("https://api.example.com/data")
data = response.json()
print(data["key"])


# Header:
import requests
headers = {"user-agent":"Myapp/1.0"}
response = requests.get("https://api.example.com/data",headers=headers)
print(response.text)

# Error Handling:
import requests
try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()
except requests.HTTPError as err:
    print("HTTP error",err)
except requests.RequestException as exp:
    print("Request error",exp)


