import os
from discord.ext import commands
from discord.ext.commands import Cog

class General(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.PREFIX = os.getenv("DISCORD_PREFIX")
    
    @commands.hybrid_command(
        name="sarasa",
        description="Solamente dice sarasaaaaaaaaa"
    )
    async def sarasa(self, ctx):
        await ctx.send("sarasaaaaaaaaa")


async def setup(bot):
    await bot.add_cog(General(bot))