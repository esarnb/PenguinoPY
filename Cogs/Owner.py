import discord
from discord.ext import commands

# Owner only commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self._last_member = None

    @commands.command(name="owner", description="Check if you are an owner")
    async def owner(self, c):
        if not (await self.bot.is_owner(c.message.author)):
            return await c.send('Seems like you are not my owner.')
        else: return await c.send("You are one of my owners!")

    @commands.command(name="kill", description="Kills bot instantly")
    async def kill(self, c):
        if not (await self.bot.is_owner(c.message.author)): await c.send('Not Authorized')
        else: 
            await c.send("Restarting...")
            await self.bot.logout()


def setup(bot):
    bot.add_cog(Owner(bot))