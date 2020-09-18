import GroupMeInterface

f = open("auth.txt", "r")
auth = f.read()
f.close()

gm = GroupMeInterface.GroupMe(auth)
print(gm.sendMessage(62656435, "message"))