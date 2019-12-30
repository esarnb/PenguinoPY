import discord
from discord.ext import commands

# Owner only commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Tools = bot.get_cog('Tools')

    @commands.command(name="owner", description="Check if you are an owner")
    async def owner(self, c):
        if not (await self.bot.is_owner(c.message.author)):
            return await c.send('Seems like you are not my owner.')
        else: return await c.send("You are one of my owners!")

    # Reload cog command
    @commands.command( name='reload', aliases=['load'], description='Reloads a command file' )
    @commands.is_owner()
    async def reload(self, c, cog):
        # Reload cog
        self.bot.reload_extension(f'Cogs.{cog.capitalize()}')
        await self.Tools.embed(c, "Reload", f'`{cog}` has been reloaded!')


    @commands.command(name="kill", description="Kills bot instantly")
    @commands.is_owner()
    async def kill(self, c):
        await c.send("Restarting...")
        await self.bot.logout()


def setup(bot):
    bot.add_cog(Owner(bot))