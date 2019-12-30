from discord.ext import commands

# Events

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.Tools = self.bot.get_cog('Tools')
        print("Ready!")

    # Throw an exception into the chat whenever there's an error
    @commands.Cog.listener()
    async def on_command_error(self, c, exc):
        # Ignore command not existing
        if 'is not found' in str(exc): return
        else: await self.Tools.error(c, 'Error', str(exc))
        print(exc)

def setup(bot):
    bot.add_cog(Events(bot))