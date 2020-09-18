import requests

groupNumber = 62656435

url = "https://api.groupme.com/v3/groups/" + str(groupNumber)+ "/messages?token="
headers = {'Content-Type': 'application/json'}
r = requests.get(url, headers=headers)

c = str(r.content)
print(c)

i0 = 0
i1 = 0

count = 0

while c.find(",\"id\":\"", i0) >= 0:
    i0 = c.find(",\"id\":\"", i0) + 1
    i1 = c.find("\",", i0)
    mID = c[i0+6:i1]

    i0 = c.find(",\"text\":\"", i0) + 1
    i1 = c.find("\",", i0)
    mess = c[i0+8:i1]


    print(mID, mess)
    count = count+1

print(count)
