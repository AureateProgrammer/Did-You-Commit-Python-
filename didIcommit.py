import requests
from datetime import date
from plyer import notification
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
    notification.notify(
        title='You have commited nice.',
        message='Your on your way to a good job.',
        timeout =10 )
else:
    notification.notify(
            title='You have not commited',
            message='Commit today so you can have a good job',
            timeout =10 )
print(today )

print(event1)
