import urllib.request
import json

url = urllib.request.urlopen("https://tmi.twitch.tv/group/user/xinvictus808x/chatters")
print(url)
data = json.loads(url.read())['chatters']
print(data)
print(data['moderators'])
for mod in data['moderators']:
	print(mod)
