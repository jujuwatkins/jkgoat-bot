import discord
from discord.ext import tasks, commands
import os
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv("TOKEN")

CHANNEL_ID = 1478166066424451218
GUILD_ID = 1478166064926818354  # your server ID

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

# 🎲 /hi command
@bot.tree.command(name="hi", description="Say hi to the bot"), guild=discord.Object(id=1478166064926818354))
async def hi(interaction: discord.Interaction):
    responses = [
        "what dumb nut",
        "what do you want",
        "hey can we meet up oh wait im a bot who feels no emotion hahah *sigh*"
    ]
    await interaction.response.send_message(random.choice(responses))


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    # 🔥 FAST sync to YOUR server only (fixes missing /hi)
    guild = discord.Object(id=GUILD_ID)
    await bot.tree.sync(guild=guild)

    print("Slash commands synced!")

    hourly_check.start()


@tasks.loop(hours=1)
async def hourly_check():
    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        if random.randint(1, 100) == 1:
            await channel.send(random.choice(MESSAGES))


bot.run(TOKEN)
