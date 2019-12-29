# Import libs
import config
import discord
from discord.ext import commands


# Useful docs: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=ctx
# Initialize "client"
client = commands.Bot(
    command_prefix=config.PREFIX,
    owner_ids=[251091302303662080],
    activity=discord.Activity(name='Netflix', type=discord.ActivityType.watching),
    case_insensitive=True
)

# Events


# Creating commands
@client.event
async def on_ready():
    print('Ready!')

# Create command called 'ping'
@client.command(name="ping", description="Shows stuff")
async def ping(c, args="args"):
    # Send to channel
    await c.send(args)

@client.command(name="status", description="Set a new bot status: (type) (phrase)", owner_only = True)
async def status(c, _type: str, *status):
    if not (await client.is_owner(c.message.author)):
        return await c.send('NO OWNER!!!!!!!!')

    await c.send(f'Type: {_type}\nStatus: {" ".join(status)}')
    await client.change_presence(activity=discord.Activity(name=" ".join(status), type=discord.ActivityType[_type]))

@client.command(name="kill", description="Kills bot instantly")
async def kill(c):
    if not (await client.is_owner(c.message.author)): await c.send('NO OWNER!!!!!!!!')
    else: await client.logout()

# Login
client.run(config.TOKEN)
