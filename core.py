# Import all the required libraries
import discord.ext.commands as discord
import discord.utils as discordutils
import random
import asyncio

# Get bot token
with open("bot-token.txt", mode="r") as f:
    token = f.readlines()[0]

# Create bot object
bot = discord.Bot(command_prefix="..")

# Initialise Commands


# Initialise Evennts
@bot.event
async def on_ready():
    print("Logged in!")
    print(f"Name: {bot.user.name}")
    print(f"ID: {bot.user.name}")
    print("~"*25)


# Start her up!
bot.run(token)