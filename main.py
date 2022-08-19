import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

@client.event
async def on_ready():
    print(f'Bot Name: {client.user} / Bot Id: {client.user.id}')
    print('Bot Online / Dev. BestHentai0')

@client.command(name='Embed')
async def ping(ctx):
    await ctx.send(embed = discord.Embed(title = 'Embed Test', description = 'This is the embed base code', color = 0xc095ff))

client.run('token')