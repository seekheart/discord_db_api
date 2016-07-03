import discord
import asyncio

client = discord.Client()
#plz don't hack me
token = 'itz a secret heheheh'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.servers)

    #get the right channel
    # TODO: keep track of right channel id..
    help_dir_channel  = None
    for server in client.servers:
        for channel in server.channels:
            if "helpdirectory" in channel.name:
                help_dir_channel = channel

    #get messages
    async for message in client.logs_from(help_dir_channel):
        print(message.content)



client.run(token)
