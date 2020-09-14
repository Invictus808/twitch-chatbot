#####
#
#	Invictus808's Twitch Chatbot
#
#	File: commands.py
#
#	Copyright: 2020, Blaise H. Aranador
#
#	Description: This file contains the functions to run the Twitch Chatbot.
#
#####

import ast
import time


# Function: loadCommands()
# Description: This function loads the dictionary of commands in a file. Returns a dictionary of the commands.
def loadCommands():
	try:
		f = open("data/commands", "r")
		commands = ast.literal_eval(f.read())
		f.close()
	except:
		commands = {}

	return commands


# Function: storeCommands(dict)
# Description: This function stores the dictionary of commands in a file.
def storeCommands(commands):
	f = open("data/commands", "w")
	f.write(str(commands))
	f.close()

	return


# Function: addCommand(str, int, str, dict)
# Description: This function adds the command to the dictionary of commands.
def addCommand(command, userlevel, output, commands):
	if command not in commands:
		commands[command] = (userlevel, output)

	return


# Function: editCommand(str, int, str, dict)
# Description: This function edits the command in the dictionary of commands.
def editCommand(command, userlevel, output, commands):
	if command in commands:
		commands[command] = (userlevel, output)

	return


# Function: deleteCommand(str, dict)
# Description: This function deletes the command from the dictionary of commands.
def deleteCommand(command, commands):
	if command in commands:
		del commands[command]

	return


# Function: countdown(int)
# Description:
def countdown(s, n):
	from channel import sendMessage

	if (n > 10) or (n < 1):
		sendMessage(s, "/me Please have countdown between 1-10 seconds")
	else:
		for i in range(n):
			sendMessage(s, str(n - i))
			time.sleep(1)
		sendMessage(s, "GO!")

	return
