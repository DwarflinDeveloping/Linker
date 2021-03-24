async def set_family(ctx, *args):
    if not ctx.channel.permissions_for(ctx.author).manage_messages:
        await ctx.send("You are not allowed to change the default guild url.\n"
                       "Confused? Try `%troubble changefamily`")
        return
    guild_family_file = open(f"data/guild_familys/{str(ctx.guild.id)}.txt", "w")
    guild_family_file.write(args[1])
    guild_family_file.close()

    await ctx.send(f"The default URL of the guild has been changed to```{args[1]}```")


async def clear_family(guild_id):
    from utils import ReturnCodes

    import os
    if os.path.isfile(f"data/guild_familys/{str(guild_id)}.txt"):
        os.remove(f"data/guild_familys/{str(guild_id)}.txt")
        return ReturnCodes.SUCCESS
    else:
        return ReturnCodes.NOT_FOUND
