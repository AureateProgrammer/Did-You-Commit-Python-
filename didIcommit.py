import requests
from datetime import date

username = "AureateProgrammer"
url = f"https://api.github.com/users/{username}/events/public"

response = requests.get(url)
events = response.json()

print(events[0])