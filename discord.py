import discord.py
from discord.ext import commands

# Discord botunuzun tokenini ve prefixini buraya girin
TOKEN = 'NTU3NjAwMzkzODI0MDQzMDE5.GOU8iv.kNONyG65VjX67yB7dhn-hB6kTdis_OwNop1zNM'
PREFIX = '!'

bot = commands.Bot(command_prefix=PREFIX)

@bot.command()
async def merhaba(ctx):
  await ctx.send('Merhaba!')

bot.run(TOKEN)
