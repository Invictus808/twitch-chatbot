#####
#
#	Invictus808's Twitch Chatbot
#
#	File: connect.py
#
#	Copyright: 2020, Blaise H. Aranador
#
#	Description: This file contains the functions to run the Twitch Chatbot.
#
#####

import os
import socket


# Function: openSocket()
# Description: This function opens a socket connection to the Twitch IRC server. Returns the socket object.
def openSocket():
	s = socket.socket()
	s.connect((os.environ['HOST'], int(os.environ['PORT'])))

	return s


# Function: authenticate(socket.socket)
# Description: This function authenticates the socket connection to the Twitch IRC server.
def authenticate(s):
	s.send(("PASS " + os.environ['OAUTH_TOKEN'] + "\r\n").encode('utf-8'))
	s.send(("NICK " + os.environ['BOT_USERNAME'] + "\r\n").encode('utf-8'))

	return
