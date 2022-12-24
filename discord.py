import discord
from discord.ext import commands

# Discord botunuzun tokenini ve prefixini buraya girin
TOKEN = 'YOUR_BOT_TOKEN'
PREFIX = '!'

bot = commands.Bot(command_prefix=PREFIX)

@bot.command()
async def merhaba(ctx):
  await ctx.send('Merhaba!')

bot.run(TOKEN)
