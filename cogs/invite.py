import disnake
from disnake.ext import commands

class InviteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        invite_link = await ctx.bot.generate_invite()
        await ctx.send(f"Invite me to your server: {invite_link}")

def setup(bot):
    bot.add_cog(InviteCog(bot))