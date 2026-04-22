import discord
from discord.ext import tasks, commands
import os
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1478166066424451218

MESSAGES = [
    "I love Cryptic Vain",
    "aew is better than wrestle btw",
    "doors is the best ROBLOX horror game",
    "Jakobe is not innocent he said those things"
    "I hate Miggers"
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    hourly_check.start()

@tasks.loop(hours=1)
async def hourly_check():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        if random.randint(1, 100) == 1:
            await channel.send(random.choice(MESSAGES))

bot.run(os.getenv("TOKEN"))
