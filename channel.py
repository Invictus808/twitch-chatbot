#####
#
#	Invictus808's Twitch Chatbot
#
#	File: channel.py
#
#	Copyright: 2020, Blaise H. Aranador
#
#	Description: This file contains the functions to run the Twitch Chatbot.
#
#####

import os
import socket
import re
import concurrent.futures as cf
from auth import *
from commands import *


# Function: joinChannel(socket.socket)
# Description: This function connects the chatbot to the Twitch channel.
def joinChannel(s):
	s.send(("JOIN #" + os.environ['CHANNEL_NAME'] + "\r\n").encode('utf-8'))

	#initialize the read buffer
	read_buffer = ""

	loading = True

	while loading:
		# read from socket 1024 bytes at a time
		read_buffer = read_buffer + s.recv(1024).decode()

		# split buffer by new lines
		lines = read_buffer.split("\n")

		readbuffer = lines.pop()

		for line in lines:
			print(line)
			loading = isLoading(line)

	sendMessage(s, "/me is now active! BloodTrail")

	return


# Function: leaveChannel(socket.socket)
# Description: This function disconnects the chatbot from the Twitch channel.
def leaveChannel(s):
	sendMessage(s, "/me is now shutting down... Have a nice day KonCha")
	s.send(("PART #" + os.environ['CHANNEL_NAME'] + "\r\n").encode('utf-8'))

	return


# Function: isLoading(str)
# Description: This function indicates whether or not the chatbot is still connecting. Returns a boolean.
def isLoading(line):
	if "End of /NAMES list\r" in line:
		return False
	else:
		return True


# Function: isPING(str)
# Description: This function indicates whether or not the Twitch IRC server sent a PING message. Returns a boolean.
def isPING(line):
	if "PING :tmi.twitch.tv\r" == line:
		return True
	else:
		return False


# Function: isPONG(str)
# Description: This function indicates whether or not the Twitch IRC server sent a PONG message. Returns a boolean.
def isPONG(line):
	if "PONG :tmi.twitch.tv\r" == line:
		return True
	else:
		return False


# Function: sendPING(socket.socket)
# Description: This function sends a PING message to the Twitch IRC Server.
def sendPING(s):
	s.send(("PING :tmi.twitch.tv\r\n").encode('utf-8'))
	print(">> SENT:PING:tmi.twitch.tv")

	return


# Function: sendPONG(socket.socket)
# Description: This function sends a PONG message to the Twitch IRC server.
def sendPONG(s):
	s.send(("PONG :tmi.twitch.tv\r\n").encode('utf-8'))
	print(">> SENT:PONG :tmi.twitch.tv")

	return


# Function: sendMessage(socket.socket, str)
# Description: This function sends a message to the Twitch channel.
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + os.environ['CHANNEL_NAME'] + " :" + message
	s.send((messageTemp + "\r\n").encode('utf-8'))
	print(">> SENT:" + message)

	return


# Function: monitorChannel(socket.socket, dict)
# Description: This function monitors the messages sent to the Twitch channel.
def monitorChannel(s):
	read_buffer = ""

	regex = ":(?P<NICK>[^ ]+?)!(?P<USER>[^ ]+?)@(?P<USER2>[^ ]+?)\.(?P<HOST>[^ ]+?) PRIVMSG \#(?P<CHANNEL>[^ ]+?) :(?P<MESSAGE>.*)\r"
	commands_regex = "-commands (?P<ACTION>[(add)|(edit)|(delete)]) (?P<COMMAND>[^ ]+?) (?P<MESSAGE>[^ ]+?)"

	commands = loadCommands()

	monitor = True

	while monitor:
		# read from socket 1024 bytes at a time
		read_buffer = read_buffer + s.recv(1024).decode()

		# split buffer by new lines
		lines = read_buffer.split("\n")

		read_buffer = lines.pop()

		for line in lines:
			#cf.ThreadPoolExecutor().submit(monitor, line)
			print("<< RECV:" + line)
			if isPING(line):
				print("is PING!")
				sendPONG(s)
			else:
				msg = re.fullmatch(regex, line)

				if msg != None:
					if (msg.group('MESSAGE') == "SERVICE IS APPRECIATED") and isPrivileged(msg.group('USER')):
						monitor = False
					elif msg.group('MESSAGE') == "-help":
						sendMessage(s, "What do you need help with?")
					elif msg.group('MESSAGE') == "-countdown":
						cf.ThreadPoolExecutor().submit(countdown, s, 5)
					elif msg.group('MESSAGE') == "-add":
						addCommand("gg", 0, "yessah blessah", commands)
					elif msg.group('MESSAGE') in commands:
						sendMessage(s, commands[msg.group('MESSAGE')][1])
					'''
					elif "-commands" in msg.group('MESSAGE'):
						print(msg.group('MESSAGE'))
						msg = re.fullmatch(commands_regex, msg.group('MESSAGE'))
						print(msg.group('ACTION'))
						if msg.group('ACTION') == "add":
							print(f"Adding {msg.group('COMMAND')} to say {msg.group('MESSAGE')}")
						elif msg.group('ACTION') == "edit":
							print(f"Editing {msg.group('COMMAND')} to say {msg.group('MESSAGE')}")
						elif msg.group ('ACTION') == "delete":
							print(f"Deleting {msg.group('COMMAND')}")
						else:
							print("ERROR: No action can be taken")
					'''

	storeCommands(commands)

	return
