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

import time
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# stores last time each user used /hi
last_hi_time = {}
COOLDOWN_SECONDS = 30

responses = [
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
    current_time = time.time()

    # check cooldown
    if user_id in last_hi_time:
        time_since = current_time - last_hi_time[user_id]

        if time_since < COOLDOWN_SECONDS:
            await interaction.response.send_message(
                "can you stop its getting annoying",
                ephemeral=True
            )
            return

    # update last used time
    last_hi_time[user_id] = current_time

    # random response
    await interaction.response.send_message(random.choice(responses))


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.tree.sync()


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
