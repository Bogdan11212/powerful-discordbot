@bot.command()
async def modify_embed(ctx):
    for cog in bot.cogs.values():
        if isinstance(cog, EmbedCog):
            await cog.modify_embed(ctx)

###########################################

class EmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def modify_embed(self, ctx):
        embed = disnake.Embed(title="Modified Title", description="Modified Description", color=disnake.Color.red())
        embed.set_author(name="Modified Author")
        embed.add_field(name="Modified Field", value="Modified Value", inline=False)
        # Modify other aspects of the embed as needed
        # ...
        await ctx.send(embed=embed)