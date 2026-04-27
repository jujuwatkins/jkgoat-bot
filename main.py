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


CHANNEL_ID = 1478166066424451218
GUILD_ID = 1478166064926818354 

# ======================
# MESSAGE SYSTEM
# ======================
MESSAGES = [
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
import discord
from discord.ext import commands
import random
import time

# 🔑 PUT YOUR BOT TOKEN HERE
TOKEN = MTQ5Mjk5OTIxOTE2MDU0NzM2OA.GYJaD8.kK8NIh7dUmFjFNu9t5bbq7MFrVzLJK-KfzNPSM

# ⚙️ BOT SETUP
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# ⏱️ COOLDOWN TRACKING
last_used = {}

# 💬 HI RESPONSES

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
# ✅ BOT READY EVENT (SYNC COMMANDS)
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

# 👋 SLASH COMMAND
@bot.tree.command(name="hi", description="Say hi")
async def hi(interaction: discord.Interaction):
    user_id = interaction.user.id
    now = time.time()

    # 🚫 cooldown check
    if user_id in last_used:
        if now - last_used[user_id] < 30:
            await interaction.response.send_message(
                "can you stop its getting annoying",
                ephemeral=True
            )
            return

    # ⏳ update time
    last_used[user_id] = now

    # 🎲 send random message
    await interaction.response.send_message(random.choice(HI_MESSAGES))

# ▶️ RUN BOT
bot.run(TOKEN)
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
