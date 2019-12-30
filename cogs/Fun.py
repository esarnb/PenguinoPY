from discord.ext import commands

# Fun Commands
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self._last_member = None

    @commands.command(name="say", alias=["speak"], description="Says input phrases")
    async def say(self, c, *args):
        await c.send(" ".join(args) if args else "No arguments provided")

def setup(bot):
    bot.add_cog(Fun(bot))