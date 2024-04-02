# The requests module in Python is a popular HTTP library that allows you to send HTTP requests easily and handle responses. It provides a more user-friendly alternative to Python's built-in urllib.request module.


import requests

# Send a GET request to a URL
response = requests.get("https://api.example.com/data")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.text)
else:
    print("Error:", response.status_code)
