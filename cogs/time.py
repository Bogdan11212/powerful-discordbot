import disnake
from disnake.ext import commands
from datetime import datetime, timezone

class TimeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def time(self, ctx, region):
        time = datetime.now(timezone.utc).astimezone().strftime('%Y-%m-%d %H:%M:%S')
        embed = disnake.Embed(title="Time Information", description=f"Current time in {region}: {time}", color=disnake.Color.green())
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(TimeCog(bot))