import discord
from discord.ext import commands, tasks
import random
import time
from datetime import datetime
import zoneinfo

# 🔑 BOT TOKEN (DO NOT SHARE THIS PUBLICLY)
TOKEN = "YOUR_BOT_TOKEN_HERE"

# 🧠 SETUP
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# ⏱️ COOLDOWN TRACKING
last_hi_used = {}

# 💬 SAFE MESSAGE POOL (EDIT THESE)
HI_MESSAGES = [
    "What do you want dick head",
        "wazzap", 
        "fuck off",
        "kill yourself",
        "shut the fuck up",
        "your IP is 676.767.676.7676",
        "you live at 67 cock lover st.",
        "I'm gonna fuck you in the ass"
]

HOURLY_MESSAGES = [
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

# 📍 CHANNEL ID (PUT YOUR CHANNEL ID HERE)
CHANNEL_ID = 1478166066424451218

# ✅ BOT READY
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

    hourly_task.start()

# 👋 /hi COMMAND WITH COOLDOWN
@bot.tree.command(name="hi", description="Say hi")
async def hi(interaction: discord.Interaction):
    user_id = interaction.user.id
    now = time.time()

    if user_id in last_hi_used:
        if now - last_hi_used[user_id] < 30:
            await interaction.response.send_message(
                "calm down lol wait 30 seconds",
                ephemeral=True
            )
            return

    last_hi_used[user_id] = now

    await interaction.response.send_message(random.choice(HI_MESSAGES))

# ⏰ HOURLY MESSAGE SYSTEM
@tasks.loop(hours=1)
async def hourly_task():
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        return

    # 1/100 chance
    if random.randint(1, 100) != 1:
        return

    # EST TIME CHECK
    now = datetime.now(zoneinfo.ZoneInfo("America/New_York"))
    hour = now.hour

    # late-night message
    if 0 <= hour < 5:
        await channel.send("dang its late")

    await channel.send(random.choice(HOURLY_MESSAGES))

# ▶️ RUN BOT
bot.run(TOKEN)
