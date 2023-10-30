@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None and after.channel.id == SPECIAL_CHANNEL_ID:
        category = after.channel.category
        new_channel = await category.create_voice_channel(f"{member.display_name}'s channel")
        await member.move_to(new_channel)
    if before.channel is not None and import disnake
from disnake.ext import commands
import os

bot = commands.Bot(command_prefix="!",
                   intents=disnake.Intents.all(),
                   help_command=None,
                   activity=disnake.Game('use /help ', status=disnake.Status.idle))

TOKEN = token # paste token here

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")

@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(TOKEN)
before.channel.id != SPECIAL_CHANNEL_ID:
        if len(before.channel.members) == 0:
            await before.channel.delete()