import discord, random
from discord.ext import commands

# Tools Commands
class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rColor = random.randint(0, 0xffffff) # Creates a random color whenever called.
        # self._last_member = None

    async def embed(self, c, title, desc):
        embed = discord.Embed(footer=title, description=desc, color=self.rColor)
        await c.send(embed=embed)

    async def error(self, c, errType='None', error='Error prompt'):
        await self.embed(c, title=f"Type: {errType}", desc=f'```css\n\n\n{error}\n```')


def setup(bot):
    bot.add_cog(Tools(bot))