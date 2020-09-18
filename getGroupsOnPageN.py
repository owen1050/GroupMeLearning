import requests

groupNumber = 62656435
count = 1
page = 1

url = "https://api.groupme.com/v3/groups?token="
headers = {'Content-Type': 'application/json'}
data = {"page" : page,"omit" : "memberships"}
page = page + 1
r = requests.get(url, headers=headers, params = data)

c = str(r.content)
print(c)
i0 = 0
i1 = 0

count = 0

while c.find("\"group_id\":\"", i0) >= 0:
    i0 = c.find("\"group_id\":\"", i0) + 1
    i1 = c.find("\",", i0)
    groupNumber = c[i0+11:i1]

    i2 = c.find("\"name\":\"", i1) + 1
    i3 = c.find("\",", i2)
    groupName = c[i2+7:i3]

    print(groupName, groupNumber)
    count = count+1

print(count)