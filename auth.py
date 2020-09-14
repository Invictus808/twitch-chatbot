#####
#
#	Invictus808's Twitch Chatbot
#
#	File: auth.py
#
#	Copyright: 2020, Blaise H. Aranador
#
#	Description: This file contains the functions to run the Twitch Chatbot.
#
#####

import os
import ast
import urllib.request
import json


# Function: loadModerators()
# Description:
def loadModerators():
	try:
		f = open("data/moderators", "r")
		moderators = ast.literal_eval(f.read())
		f.close()
	except:
		moderators = []

	return moderators


# Function: storeModerators(list)
# Description:
def storeModerators(moderators):
	f = open("data/moderators", "w")
	f.write(str(moderators))
	f.close()

	return


# Function: loadChatters()
# Description:
def loadChatters():
	url = urllib.request.urlopen("https://tmi.twitch.tv/group/user/" + os.environ['CHANNEL_NAME'] + "/chatters")
	chatters = json.loads(url .read())['chatters']

	return chatters


# Function: isBroadcaster(str)
# Description:
def isBroadcaster(user):
	chatters = loadChatters()

	if user in chatters['broadcaster']:
		return True
	else:
		return False


# Function: isVip(str)
# Description:
def isVip(user):
	chatters = loadChatters()

	if user in chatters['vips']:
		return True
	else:
		return False


# Function: isModerator(str)
# Description:
def isModerator(user):
	chatters = loadChatters()

	if user in chatters['moderators']:
		return True
	else:
		return False


# Function: isStaff(str)
# Description:
def isStaff(user):
	chatters = loadChatters()

	if user in chatters['staff']:
		return True
	else:
		return False


# Function: isAdmin(str)
# Description:
def isAdmin(user):
	chatters = loadChatters()

	if user in chatters['admins']:
		return True
	else:
		return False


# Function: isGlobalMod(str)
# Description:
def isGlobalMod(user):
	chatters = loadChatters()

	if user in chatters['global_mods']:
		return True
	else:
		return False


# Function:	isViewer(str)
# Description:
def isViewer(user):
	chatters = loadChatters()

	if user in chatters['viewers']:
		return True
	else:
		return False


# Function: isPrivileged(str)
# Description:
def isPrivileged(user):
	if isBroadcaster(user) or isModerator(user) or isStaff(user) or isAdmin(user) or isGlobalMod(user):
		return True
	else:
		return False
