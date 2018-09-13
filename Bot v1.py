import discord
import asyncio
import time
import random

client = discord.Client() 

async def status_task():
    while True:
        await client.change_presence("with the real Spyro")
        await asyncio.sleep(20)
        await client.change_presence("catch with a hand grenade")
        await asyncio.sleep(20)

      
async def chat(channel, message=None, tts=False, embed=None):
    if message == None and embed == None:
        return False
    else:
        try:
            msg = await client.send_message(channel, message=message, tts=tts, embed=embed)
            return msg
        except discord.errors.Forbidden:
            print('The bot is not allowed to send messages to this channel')
            return None
        
@client.event
async def on_ready():
    print("SpyroBot status: ONLINE")
    client.loop.create_task(status_task())
    
@client.event
async def on_message(message):
    author = message.author
    ch = message.channel
    server = message.server
    
    arguments = message.content.split(' ')
    command = arguments[0].lower()
    
    while len(arguments) < 15:
        arguments.append('')
    else:
        pass # wow
    
    # TODO: rewrite the rest of the on_message function to use the new chat function, and use the variables created above
    
    if message.content == "Who is the best streamer?":  #this checks to see if someone has sent a message with the same text that is in the ""
        await client.send_message(message.channel, "Obviously its SpyroL7")  #if the above statement = true, the bot sends the message in the ""
                                #message.channel means the text is posted in the same channel as the trigger message was sent in
    if message.content == "Who is the worst streamer?":  
        await client.send_message(message.channel, "Matt65 lol")
    if message.content == "Alexa play despacito".lower():  
        await client.send_message(message.channel, " ```Playing Despacito by Louis Fonsi ft. Daddy Yankee``` ")
    if message.content == "Press F to pay respects":  
        await client.send_message(message.channel, "F")
    if message.content == "Who is the best bot":  
        await client.send_message(message.channel, "Well thats me of course! Want to add me to your server? Here's a link: https://discordapp.com/api/oauth2/authorize?client_id=483591622425051136&permissions=8&scope=bot ")
    if message.content == "Good bot":  
        await client.send_message(message.channel, "*excited borking*")
    if message.content == "Bad bot":  
        await client.send_message(message.channel, "Well fuck you too")
    if message.content == "@Spyroboto#4192 ":  
        await client.send_message(message.channel, "omg what. Like seriously did you have to ping me? I was taking a cyber nap and you woke me. pings are SO ANNOYING - like especially going live ones, but at least you can supress @ everyones. Did I tell you about the time I got banned from a server with like 30k people? Its true! I was kicked a fair bit before permabanned. Spyro didn't have admin privs, but i did so he just told me to kick people he didn't like lol. I woulda gotten away with it if it weren't for those meddling ~~kids~~ audit logs. Sorry for rambling a bit hope you enjoyed smash like, subscribe, follow and donate all your money. All of it. Right now. Pls :3 ")
    if message.content == ";-;":  
        await client.send_message(message.channel, "this")
        time.sleep(0.3)
        await client.send_message(message.channel, "is")
        time.sleep(0.3)
        await client.send_message(message.channel, "so")
        time.sleep(0.3)
        await client.send_message(message.channel, "sad")
    if message.content == "cool story bro":  
        await client.send_message(message.channel, "tell it again")
    if message.content == "Indeed":  
        await client.send_message(message.channel, "Good meme")
    if message.content == "":  
        await client.send_message(message.channel, "F")
    if message.content == "This is so sad":  
        await client.send_message(message.channel, ";-;")
    if message.content == "Alexa":  
        await client.send_message(message.channel, " ```wtf do you want``` ")
    if message.content == "Despacito":  
        await client.send_message(message.channel, " ```Ew``` ")
    if message.content == "Hello":  
        await client.send_message(message.channel, "Go away no one likes you")
    if message.content == "yeet":  
        await client.send_message(message.channel, "ok hold up. Did you seriously just say yeet? like what are you, 10 years old? Have you only 3 working brain cells?! Like there must be something genuinely wrond with your brain. When was the last time you had it scanned. Really brings back memories of LONG DEAD MEMES. I mean, 2016 may have been a better time but like do you remember the quilaity of memes? Like that gorilla - all it did was DIE and it became a meme?! Like if that was how it is now i would be liking more of those 'like to instantly die' memes ")
    if message.content.startswith('Shrek'):
        await client.kick(message.author)
    




client.run("TOKEN")   #the bots token - used to connect the script and the app
