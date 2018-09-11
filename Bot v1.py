import discord
import asyncio
import time
import random

client = discord.Client() 

if True: #this lets you fold the code is supported editors to take less room
    presences = [ # add any texts you want here. This is valid syntax, as long as you end the list with the ] properly
        "with the Real Spyro",
        "with your emotions",
        "catch with a grenade",
        "contemplating suicide"
    ]
    
    presenceChangeTime = 20 # increased from 10 because 10 seconds is too short

async def status_task():
    global client
    global presences
    global presenceChangeTime
    while True:
        newPresence = discord.Game(name=random.choice(presences))
        await client.change_presence(game=newPresence)
        await asyncio.sleep(presenceChangeTime)
        
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
    if message.content == "Who is the sweetest Dutch boy?":
        await client.send_message(message.channel, "Obviously Niek!")
    if message.content == "Who is the most tired person ever?"):
        await client.send_message(message.channel, "Xochipilli...")
    if message.content == "Who is blessed?"):
        await client.send_message(message.channel, "You are blessed! Yeehaw :)")
    if message.content == "Hello":  
        await client.send_message(message.channel, "Go away no one likes you")
    if message.content.startswith('Shrek'):
        await client.kick(message.author)


    #I'm hoping to make a 'help' function, so let's see what happens. - xochipilli
    #Commented out so it doesn't mess with the bot.
    if message.content == "Help":
        await client.send_message(message.channel, "No thanks :)")
    
    #I'm not sure if the below will work, because I'm adapting it from another source, but we'll see.
    #class CommandHandler:

    # create the CommandHandler object and pass it the client
    #ch = CommandHandler(client)
    
    # constructor
    #def __init__(self, client):
    #    self.client = client
    #    self.commands = []

    #def add_command(self, command):
    #    self.commands.append(command)

    #def command_handler(self, message):
    #    for command in self.commands:
    #        if message.content.startswith(command['s!']):
    #            args = message.content.split(' ')
    #            if args[0] == command['s!']:
    #                args.pop(0)
    #                if command['args_num'] == 0:
    #                    return self.client.send_message(message.channel,str(command['function'](message, self.client, args)))
    #                    break
    #                else:
    #                    if len(args) >= command['args_num']:
    #                        return self.client.send_message(message.channel,str(command['function'](message, self.client, args)))
    #                        break
    #                    else:
    #                        return self.client.send_message(message.channel, 'command "{}" requires {} argument(s) "{}"'.format(command['trigger'], command['args_num'], ', '.join(command['args_name'])))
    #                        break
    #            else:
    #                break      
    
    #def help_function(message, client, args):
    #try:
    #    return 'Hello {}, Argument One: {}'.format(message.author, args[0])
    #except Exception as e:
    #    return e
    #ch.add_command({
    #'s!': 'help',
    #'function': help_function,
    #'args_num': 1,
    #'args_name': ['string'],
    #'description': 'Will respond with helpful information.'
    

client.loop.create_task(status_task())
client.run("<TOKEN>")   #the bots token - used to connect the script and the app
