#####
#
#	Invictus808's Twitch Chatbot
#
#	File: bot.py
#
#	Copyright: 2020, Blaise H. Aranador
#
#	Description: This file contains the functions to run the Twitch Chatbot.
#
#####

from connect import openSocket, authenticate
from channel import joinChannel, monitorChannel, leaveChannel


# Description: This is the execution sequence for this file.
if __name__ == "__main__":
	s = openSocket()
	authenticate(s)
	joinChannel(s)
	monitorChannel(s)
	leaveChannel(s)
