# Invictus808's Twitch Chatbot

## Virtual Environment: Pipenv
### Environment File
The *.env* file contains all the environment variables such as **BOT_USERNAME**, **OAUTH_TOKEN**, etc.

### Pipfile
The *Pipfile* contains all the packages needed to run the Twitch chatbot.


## Python Files
### auth.py
The *auth.py* file contains the code used to obtain all the chatters in the Twitch channel and check the role each chatter has.


### bot.py
The *bot.py* file contains the code used to run the Twitch Chatbot.


### channel.py
The *channel.py* file contains the code used to connect, monitor, and disconnect from the Twitch channel. This file also contains the code used to send messages to the Twitch IRC server and Twitch channel.


### commands.py
The *commands.py* file contains the code used to load, store, add, edit, and delete commands.


### connect.py
The *connect.py* file contains the code used to connect and authenticate the chatboat to the Twitch IRC server.
