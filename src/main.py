import discord
from discord.ext import commands


client = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@client.event
async def on_ready():
    try:
        await client.tree.sync()
    except:
        pass

    print('Bot is ready')


@client.tree.command(name="etest",description="nothing")
async def etest(inter:discord.Interaction):
    await inter.response.send_message("Hello World")


client.run("")