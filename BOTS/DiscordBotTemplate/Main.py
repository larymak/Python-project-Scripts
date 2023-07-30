import discord
import os
from random import randint

TOKEN = "" #place your bots token here

bot = discord.Bot() #defines the bot

#this event will print to the console when the bot is running and ready for commands
@bot.event
async def on_ready():
    print(f'{bot.user} is ready')

#below are the commands, have fun with it, you are only limited by your imagination

#Example command, test it in your server using /hello
@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

#another example, here the bot will provide a random number between 1 and 10. 
@bot.slash_command(name = "random", description = "get a random number between 1 and 10")
async def random(ctx):
    await ctx.respond(randint(1,10))


bot.run(TOKEN) #this line is what runs the bot itself