import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!', intents=intents, enale_debug_events=True)

sureler = []

@bot.event
async def on_ready():
    print('TurkishBot is ready!')


@bot.command()
async def ayet(ctx, sure: str, ayet: int):
    #TODO
    None
@bot.command()
async def hadis(ctx, kitap: str, no: str):
    if kitap is not 'Buhari' or 'Müslim':
        await ctx.send('Gecerli bir hadis kitabi belirtmediniz.')
    #TODO
    
    
    