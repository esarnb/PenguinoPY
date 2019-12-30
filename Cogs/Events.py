from discord.ext import commands

# Events

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready!")

def setup(bot):
    bot.add_cog(Events(bot))