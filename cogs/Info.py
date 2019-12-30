import discord
from discord.ext import commands

# Informative Commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self._last_member = None

    @commands.command(name="ping", alias=["pong"], description="Returns latency")
    async def ping(self, c):
        await c.send(embed=discord.Embed(
            description=f'❄ Latency: {round(self.bot.latency, 2)}ms'
        ))
    
    
    @commands.command(name="status", description="Set a new bot status: (type) (phrase)", owner_only = True)
    async def status(self, c, _type: str, *status):
        if not (await self.bot.is_owner(c.message.author)):
            return await c.send('Not Authorized')

        await c.send(f'Type: {_type}\nStatus: {" ".join(status)}')
        await self.bot.change_presence(activity=discord.Activity(name=" ".join(status), type=discord.ActivityType[_type]))

def setup(bot):
    bot.add_cog(Info(bot))