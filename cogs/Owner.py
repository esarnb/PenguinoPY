import discord, os
from discord.ext import commands

# Owner only commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Tools = bot.get_cog("Tools")

    # Check if the user is in the owner's list
    @commands.command(name="owner", description="Check if you are an owner")
    async def owner(self, c):
        await c.send("You are one of my owners!" if self.bot.is_owner(c.message.author) else "Seems like you are not my owner.")

    # Set a new status for the bot
    @commands.command(name="status", description="Set a new bot status: (type) (phrase)", owner_only = True)
    @commands.is_owner()
    async def status(self, c, _type: str, *status):
        await c.send(f"Type: {_type}\nStatus: {' '.join(status)}")
        await self.bot.change_presence(activity=discord.Activity(name=" ".join(status), type=discord.ActivityType[_type]))

    # Reload cog command
    @commands.command(name="reload", aliases=["load", "restart"], description="Reloads a command file")
    @commands.is_owner()
    async def reload(self, c, cog):
        # Reload all commands by iteration if parameter cog == all, else just reload the cog filename.
        [self.bot.reload_extension(f"cogs.{f.replace('.py', '')}") for f in os.listdir("cogs") if not f.startswith("__")] if cog.lower() == "all" else self.bot.reload_extension(f"cogs.{cog.capitalize()}")
        await self.Tools.embed(c, "Reload command", f"`{cog}` cog reloaded!", discord.Colour.red())

    # kill the script with a discord logout
    @commands.command(name="kill", description="Kills bot instantly")
    @commands.is_owner()
    async def kill(self, c):
        await c.send("Restarting...")
        await self.bot.logout()

def setup(bot):
    bot.add_cog(Owner(bot))
