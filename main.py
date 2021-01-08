import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    isBotModerator = "botmoderator" in [i.name for i in message.author.roles]

    if message.author == client.user:
        return

    if message.content.startswith('$hello') and isBotModerator:
        msg = "Hello admin! Nice to meet You. Let's get some work done!"
        await message.channel.send(msg)

    if message.content == "$kick":
        await message.channel.send("Kicked Who?")

@client.event
async def on_disconnect():
    print("Bot Disconnected !") ## Will print in our console not in discord chat.

client.run('Token')
