import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix = "Sp/")   #certain commands that require a bot prefix must start with the prefix in the ""

async def status_task():
    while True:
        await client.change_presence("with the Real spyro")
        await asyncio.sleep(10)
        await client.change_presence("with your emotions")
        await asyncio.sleep(10)
        await client.change_presence("catch with a grenade")
        await asyncio.sleep(10)
        await client.change_presence("contemplating suicide")
        await asyncio.sleep(10)

@client.event
async def on_ready():
    print("SpyroBot status: ONLINE")   #if the bot is online, it sends this message
    client.loop.create_task(status_task())
    
    
@client.event
async def on_message(message):
    if message.content == "Who is the best streamer?":  #this checks to see if someone has sent a message with the same text that is in the ""
        await client.send_message(message.channel, "Obviously its SpyroL7")  #if the above statement = true, the bot sends the message in the ""
                                #message.channel means the text is posted in the same channel as the trigger message was sent in
    if message.content == "Who is the worst streamer?":  
        await client.send_message(message.channel, "Matt65 lol")
    if message.content == "Alexa play despacito":  
        await client.send_message(message.channel, " ```Playing Despacito by Louis Fonsi ft. Daddy Yankee``` ")
    if message.content == "Press F to pay respects":  
        await client.send_message(message.channel, "F")
    if message.content == "This is so sad":  
        await client.send_message(message.channel, ";-;")
    if message.content == "Alexa":  
        await client.send_message(message.channel, " ```wtf do you want``` ")
    if message.content == "Despacito":  
        await client.send_message(message.channel, " ```Ew``` ")
    if message.content == "Hello":  
        await client.send_message(message.channel, "Go away no one likes you")
    if message.content.startswith('Shrek'):
        await client.kick(message.author)



    


client.run("NDgzNTkxNjIyNDI1MDUxMTM2.Dmw9Mg._smm7HVKuuJXNG0M4KUl4KmsTjs")   #the bots token - used to connect the script and the app
