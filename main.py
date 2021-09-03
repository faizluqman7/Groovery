import discord
from discord.ext import commands
from webserver import keep_alive
import os
import music

my_secret = os.environ['TOKEN']

client = commands.Bot(command_prefix='-')

cogs = [music]
for i in range(len(cogs)):
	cogs[i].setup(client)
	
	
keep_alive()
client.run(my_secret)	