import discord, logging
from discord.ext import commands

logger = logging.getLogger(__name__)

# Events

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Tools = self.bot.get_cog("Tools")

    # Discord Event Ready() will run once the bot has logged into the service
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.reload_extension("cogs.Events")
        print("Ready!")

    # Throw an exception into the chat whenever there's an error
    @commands.Cog.listener()
    async def on_command_error(self, c, exc):
        if isinstance(exc, commands.CommandNotFound): return # If command is not found, don't print anything.
        await self.Tools.error(c, err=f"```xl\n{str(exc)}\n```", _type="Command Error Handler", colour=discord.Colour.red())
        
def setup(bot):
    bot.add_cog(Events(bot))