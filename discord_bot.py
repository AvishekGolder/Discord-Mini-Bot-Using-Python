import discord
from discord.ext import commands,tasks
from random import choice
import googletrans
from googletrans import Translator






bot = commands.Bot(command_prefix='.')
status = ['Chilling with music','sleeping','jamming','eating']



@bot.event
async def on_ready():
    change_status.start()
    print("Bot is online")


@bot.command(name='ping', help='This command returns the ping')
async def ping(ctx):
    await ctx.send(f'**Hey!** Latency:{round(bot.latency * 1000)},ms')

@bot.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
    responses = ['how are you', 'hlw!', 'Hello, how are you?', 'Hi', 'whats up']
    await ctx.send(choice(responses))


@bot.command(name='info', help='This command returns the developers info')
async def info(ctx):
    await ctx.send('Made by `Avishek Golder`')
    await ctx.send('Details: `github.com/avishekgolder`')

@bot.command(name="trans", help='This command translate anything | Example .trans bn You are a good guy')
async def translate(ctx, lang, *, args):
    t = Translator()
    a = t.translate(args, dest=lang)
    await ctx.send(a.text)


@tasks.loop(seconds=10)
async def change_status ():
    await bot.change_presence(activity=discord.Game(choice(status)))
bot.run(' ')#use your bot's token
