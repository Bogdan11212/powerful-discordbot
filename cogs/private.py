@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None and after.channel.id == SPECIAL_CHANNEL_ID:
        category = after.channel.category
        new_channel = await category.create_voice_channel(f"{member.display_name}'s channel")
        await member.move_to(new_channel)
    if before.channel is not None and before.channel.id != SPECIAL_CHANNEL_ID:
        if len(before.channel.members) == 0:
            await before.channel.delete()