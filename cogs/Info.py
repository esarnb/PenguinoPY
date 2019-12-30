import discord
from discord.ext import commands

# Informative Commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Tools = bot.get_cog("Tools")
    
    # Return's the delay between discord and the bot (latency)
            # To Do: Add msg edit delays
    @commands.command(name="ping", aliases=["pong"], description="Returns latency")
    async def ping(self, c):
        await self.Tools.embed(c, "Pong!", f"❄ Latency : {round(self.bot.latency, 2)}s ❄")
    
def setup(bot):
    bot.add_cog(Info(bot))