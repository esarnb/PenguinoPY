# Useful docs: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=ctx
# Learning from:
#  -https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
#  -https://github.com/MoistSenpai/Neptune-PY

# Import libs
import config, discord, os
from discord.ext import commands

# To DO: # Incorporate Mongo DB for prefixes

# Initialize bot with own default values
bot = commands.Bot(
    command_prefix=config.PREFIX,
    owner_ids=[251091302303662080, 184157133187710977], # 1. Myself, 2. AB0529
    activity=discord.Activity(name="Netflix", type=discord.ActivityType.watching),
    case_insensitive=True
)

# Load cogs files from Cogs directory # One-Liner Created by SoulSink 
[bot.load_extension(f"cogs.{f.replace('.py', '')}") for f in os.listdir("cogs") if not f.startswith("__")]

# Log into the discord service with the bot token
bot.run(config.TOKEN)
