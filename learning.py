import requests

url = "https://api.groupme.com/v3/groups/45105307/messages?token=rr5bwRAoMhEgSfEeTAqamDzJfo5XubTnQDlehC2P"
headers = {'Content-Type': 'application/json'}
data = {"text": "Test", "source_guid" : "6"}
r = requests.post(url, headers=headers, data = data)
print(r.content)

#https://dev.groupme.com/docs/v3#groups