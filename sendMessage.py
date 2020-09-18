import requests, time

messageNumber = round(time.time())
groupNumber = 62656435
messageText = "message text"

messageNumber = round(time.time())
url = "https://api.groupme.com/v3/groups/" + str(groupNumber)+ "/messages?token="
headers = {'Content-Type': 'application/json'}
data = {"message" : {"source_guid" : str(messageNumber), "text": messageText}}
r = requests.post(url, headers=headers, json = data)
print(r.content)

