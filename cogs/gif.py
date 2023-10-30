import disnake
from disnake.ext import commands
import requests
from bs4 import BeautifulSoup
import random

class GifCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gif(self, ctx):
        url = "https://example.com"  # Replace with the URL of the website with random gifs
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        gifs = soup.find_all('img')
        gif = random.choice(gifs)
        embed = disnake.Embed(title="Random GIF", color=disnake.Color.gold())
        embed.set_image(url=gif['src'])
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(GifCog(bot))