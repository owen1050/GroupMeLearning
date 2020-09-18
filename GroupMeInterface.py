import requests, time

class GroupMe:

    def __init__(self, auth):
        self.auth = auth
        self.baseUrl = "https://api.groupme.com/v3/"

    def likeMessage(self, groupNumber, messageID, likeBool):
        like = likeBool

        if like:
            likeStr = "like"
        else:
            likeStr = "unlike"

        url = self.baseUrl + "messages/" + str(groupNumber)+ "/"+ str(messageID)+"/"+likeStr+"?token=" + self.auth
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, headers=headers)

        return str(r.content)

    def getGroups(self, page):
        url = self.baseUrl + "groups?token=" + self.auth
        headers = {'Content-Type': 'application/json'}
        data = {"page" : page,"omit" : "memberships"}
        r = requests.get(url, headers=headers, params = data)

        c = str(r.content)
        i0 = 0
        i1 = 0

        count = 0
        groups = {}

        while c.find("\"group_id\":\"", i0) >= 0:
            i0 = c.find("\"group_id\":\"", i0) + 1
            i1 = c.find("\",", i0)
            groupNumber = c[i0+11:i1]

            i2 = c.find("\"name\":\"", i1) + 1
            i3 = c.find("\",", i2)
            groupName = c[i2+7:i3]

            groups[groupNumber] = groupName
            count = count+1

        return groups

    def getMessages(self, groupID):
        groupNumber = groupID

        url = self.baseUrl + "groups/" + str(groupNumber)+ "/messages?token=" + self.auth
        headers = {'Content-Type': 'application/json'}
        r = requests.get(url, headers=headers)

        c = str(r.content)

        i0 = 0
        i1 = 0

        count = 0
        messages = {}
        while c.find(",\"id\":\"", i0) >= 0:
            i0 = c.find(",\"id\":\"", i0) + 1
            i1 = c.find("\",", i0)
            mID = c[i0+6:i1]

            i0 = c.find(",\"text\":\"", i0) + 1
            i1 = c.find("\",", i0)
            mess = c[i0+8:i1]

            messages[mID] = mess
            count = count+1

        return messages

    def sendMessage(self, groupID, text):
        messageNumber = round(time.time() * 100)
        groupNumber = groupID
        messageText = text

        url = self.baseUrl + "groups/" + str(groupNumber)+ "/messages?token=" + self.auth
        headers = {'Content-Type': 'application/json'}
        data = {"message" : {"source_guid" : str(messageNumber), "text": messageText}}
        r = requests.post(url, headers=headers, json = data)
        return str(r.content)