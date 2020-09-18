import requests

groupNumber = 62656435
messageID = 160040516360754077
like = True

if like:
    likeStr = "like"
else:
    likeStr = "unlike"

url = "https://api.groupme.com/v3/messages/" + str(groupNumber)+ "/"+ str(messageID)+"/"+likeStr+"?token="
headers = {'Content-Type': 'application/json'}
r = requests.post(url, headers=headers)

c = str(r.content)
print(c)
