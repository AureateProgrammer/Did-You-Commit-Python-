import requests
from datetime import date

username = "AureateProgrammer"
url = f"https://api.github.com/users/{username}/events/public"

response = requests.get(url)
events = response.json()

today = str(date.today())
commited_today = False

for event1 in events:
    if event1["type"] =='PushEvent' and event1["created_at"].startswith(today):
        commited_today = True
if commited_today == True:
    print ('Yay')
else:
    print('noo')
    


print(today )
print(events[1])
