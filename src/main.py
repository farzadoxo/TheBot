import discord
from discord.ext import commands
from Assets.Messages import EventMessage
from colorama import Fore

client = commands.Bot(command_prefix='!',intents=discord.Intents.all())


# ----------------- Events ----------------- 

@client.event
async def on_connect():
    print(Fore.WHITE+"-"*50+Fore.RESET)
    print(Fore.LIGHTGREEN_EX+EventMessage.on_connect+Fore.RESET)



@client.event
async def on_resumed():
    print(Fore.WHITE+"-"*50+Fore.RESET)
    print(Fore.LIGHTYELLOW_EX+EventMessage.on_resumed+Fore.RESET)



@client.event
async def on_ready():
    try:
        await client.tree.sync()
    except Exception as error:
        print(Fore.WHITE+"-"*50+Fore.RESET)
        print(Fore.RED+error+Fore.RESET)

    print(Fore.WHITE+"-"*50+Fore.RESET)
    print(Fore.LIGHTBLUE_EX+EventMessage.on_ready+Fore.RESET)





@client.tree.command(name="help",description="🍕 Need help?")
async def help(interaction:discord.Interaction):
    interaction.response.send_message()



# run client
client.run("")