#!/usr/bin/env python
"""
Discord Bot
"""

import discord
import asyncio
from parser_class import Parser
import database

#Setup the discord bot here
client = discord.Client()
token = 'MTk4OTMwNDMyNDg0NTczMTg0.Clr70w.SgQV-SK9VKYOFgFkC1pK3QyXwP0'

#open a global db connection
my_db = database.db('localhost', 27017, 'helpTest')

#initialize our bot and log our bot in to discord
@client.event
async def on_ready():
    #login message for bot
    print('Logged in as{}'.format(client.user.name))

    #look for help directory channel
    help_dir_channel  = None
    for server in client.servers:
        for channel in server.channels:
            if "helpdirectory" in channel.name:
                help_dir_channel = channel

    #get the messages --> list of dicts {msg: usr}
    result = []
    async for message in client.logs_from(help_dir_channel):
              temp = { 'message': message.content, 'user': message.author.name }
              result.append(temp)

    #Instantiate our parser obj and parse results
    my_parser = Parser(result)
    results = my_parser.check()

    for element in results:
        try:
            user = element['user']
        except KeyError as e:
            print('No User Detected Skipping...')
            continue

        membership_li = element['membership']
        my_db.add_user(user, membership_li)

#listen for a specific message to initiate bot commands
@client.event
async def on_message(message):
    response = ''
    if message.content.startswith('!bot help'):
        # !bot help python => [!bot, help, python]
        lang = message.content.split()[2]
        user_results = my_db.get_users(lang)
        online_users = []
        #check to see who is online, and return
        #the response message with users online
        for member in message.server.members:
            for user in user_results:
                if member.name == user and member.status == member.status.online:
                    online_users.append(member.mention)

        response = print_message(online_users, lang)
        await client.send_message(message.channel,
                                                    response)

def print_message(user_results, lang):
    """
    Response message handler
    takes the list of users and returns a formatted response
    message.
    """
    main_message = 'Here is the list of pros in {}:'.format(lang)
    for user in user_results:
        main_message += '\n{}'.format(user)

    return main_message



client.run(token)
