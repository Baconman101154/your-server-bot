import discord
from discord.ext import commands
from discord.utils import get

import botinfo

client = commands.Bot(command_prefix = botinfo.prefix)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"!help | {len(client.guilds)} servers"))
    print("Bot now online")

@client.command()
async def ping(ctx):
    Embed = discord.Embed(title="PONG!", description="This shows the PING of the bot/ server", color = discord.Color.blue())
    Embed.add_field(name="Bot Latency", value=f"`{client.latency}`")
    Embed.add_field(name="Bot Latency In MS", value=f"`{round(client.latency * 1000)}ms`")
    Embed.set_footer(text="Here is all the information you need to know!")

    await ctx.send(embed=Embed)

@client.command(pass_context=True)
async def help(ctx):
    Embed = discord.Embed(title="Help", description="This is the help page for the YourServer Bot", color = discord.Color.blue())
    Embed.add_field(name="!ping", value="It say's what its ping to the discord server is!")

    await ctx.author.send(embed=Embed)


client.run(botinfo.token)