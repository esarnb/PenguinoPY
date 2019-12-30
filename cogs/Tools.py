import discord, random
from discord.ext import commands

# Tools Commands
class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self._last_member = None

    # Generate a random color everytime the function is called
    def rColor(self): return random.randint(0, 0xffffff)

    # Create a quick embed with a title,desc, and optional specific color
    async def embed(self, c, title, desc, colour=""):
        colour = self.rColor() if not colour else colour # Cannot set default parameter colour=self.rColor
        await c.send(embed= discord.Embed(title=title, description=desc, color=colour))

    # Parse an error into an embed and send it to the channel 
    async def error(self, c, _type="None", err="Error prompt", colour=discord.Colour.red()):
        await self.embed(c, _type, err)

def setup(bot):
    bot.add_cog(Tools(bot))