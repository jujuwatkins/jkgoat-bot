import discord
from discord.ext import commands, tasks
import random
import time
import os

# ======================
# INTENTS + BOT SETUP
# ======================
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv("TOKEN")

# ======================
# IDS (CHANGE THESE)
# ======================
CHANNEL_ID = 1478166066424451218
GUILD_ID = 1478166064926818354

# ======================
# MESSAGE SYSTEM
# ======================
MESSAGES =  [
    "I love Crying Tip A. Vane",
    "AEW is better than WRESTLE! and you aren't changing my mind",
    "I hate Lip",
    "Jakobe was born yesterday",
    "MJF is the goat",
    "I farted",
    "Mulberry County is better than Doors",
    "Doom Doom Doom Sahur",
    "0 big booty latinas 😭😭😭😭"
    "I nutted",
    "fuck shit bitch damn cock sucker pussy asshole cunt",
    "Elder loves penis",
    "migger"
]   

# ======================
# /HI SYSTEM
# ======================
last_hi_time = {}
COOLDOWN_SECONDS = 30

hi_responses = [
    "What do you want dick head",
        "wazzap", 
        "fuck off",
        "kill yourself",
        "shut the fuck up",
        "your IP is 676.767.676.7676",
        "you live at 67 cock lover st.",
        "I'm gonna fuck you in the ass"
]

@bot.tree.command(name="hi", description="Say hi to the bot")
async def hi(interaction: discord.Interaction):
    user_id = interaction.user.id
    now = time.time()

    # cooldown check
    if user_id in last_hi_time:
        if now - last_hi_time[user_id] < COOLDOWN_SECONDS:
            await interaction.response.send_message(
                "can you stop its getting annoying",
                ephemeral=True
            )
            return

    last_hi_time[user_id] = now

    await interaction.response.send_message(random.choice(hi_responses))

# ======================
# ON READY (IMPORTANT FIX)
# ======================
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    # 🔥 THIS FIXES /hi NOT SHOWING
    guild = discord.Object(id=GUILD_ID)
    await bot.tree.sync(guild=guild)

    print("Slash commands synced!")

    hourly_message.start()

# ======================
# HOURLY 1/100 MESSAGE
# ======================
@tasks.loop(hours=1)
async def hourly_message():
    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        if random.randint(1, 100) == 1:
            await channel.send(random.choice(MESSAGES))

# ======================
# RUN BOT
# ======================
bot.run(TOKEN)
