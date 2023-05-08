import requests
import json

# Set the URL for the Flask server
url = 'http://localhost:8000/sort_numbers'

# Define the list of numbers to send in the request body
numbers = [3, 1, 4, 1, 5, 9, 6, 5, 4,  3, 5]
payload = {'numbers': numbers}

# Send a POST request to the server with the list of numbers
response = requests.post(url, json=payload)
print(response)

# Parse the sorted list of numbers from the response JSON
sorted_numbers = json.loads(response.text)

# Print the sorted list of numbers
print(sorted_numbers)