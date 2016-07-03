import discord
import asyncio
import parser_class


client = discord.Client()
token = 'MTk4OTMwNDMyNDg0NTczMTg0.Clr70w.SgQV-SK9VKYOFgFkC1pK3QyXwP0'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)

    help_dir_channel  = None
    for server in client.servers:
        for channel in server.channels:
            if "helpdirectory" in channel.name:
                help_dir_channel = channel

    result = []
    async for message in client.logs_from(help_dir_channel):
              temp = { 'message': message.content, 'user': message.author.name }
              result.append(temp)

    MyParserClass = parser_class.ParserClass(result)
    results = MyParserClass.check()

    my_db = db('localhost', 27017, 'helpTest')

# @client.event
# async def on_message(message):



client.run(token)
