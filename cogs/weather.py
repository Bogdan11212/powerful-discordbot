import disnake
from disnake.ext import commands
import requests

class WeatherCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weather(self, ctx, region):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={region}&appid=YOUR_API_KEY"
        response = requests.get(url)
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        embed = disnake.Embed(title="Weather Information", color=disnake.Color.blue())
        embed.add_field(name="Region", value=region, inline=False)
        embed.add_field(name="Temperature", value=f"{temperature}°C", inline=False)
        embed.add_field(name="Description", value=description, inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(WeatherCog(bot))