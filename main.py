import discord
from discord.ext import tasks, commands
import os
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1478166066424451218

MESSAGES = [
    "I love Crying Tip A. Vane",
    "AEW is better than WRESTLE! and you aren't changing my mind",
    "I hate Lip",
    "Jakobe was born yesterday",
    "MJF is the goat",
    "I farted",
    "Mulberry County is better than Doors",
    "Doom Doom Doom Sahur",
    "0 big booty latinas 😭😭😭😭",
    "I nutted",
    "fuck shit bitch damn cock sucker pussy asshole cunt",
    "Elder loves penis",
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    hourly_check.start()

@tasks.loop(hours=1)
async def hourly_check():
    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        # 1/100 chance
        if random.randint(1, 100) == 1:
            await channel.send(random.choice(MESSAGES))

bot.run(os.getenv("TOKEN"))
