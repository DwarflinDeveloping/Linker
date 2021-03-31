async def manage_request(ctx, *args, client):
    args = [arg.lower() for arg in args]
    if args[0] == "get" or args[0] == "query":
        from utils import ReturnCodes

        get_family_process = get_family(ctx.guild.id)
        if get_family_process == ReturnCodes.NOT_FOUND:
            await ctx.send("This guild has no default url.")
        else:
            await ctx.send(f"The default url of this guild is:```{get_family_process}```")
    elif not ctx.channel.permissions_for(ctx.author).manage_messages:
        await ctx.send("You are not permitted to do that!")
        return
    elif args[0] == "set":
        if len(args) != 2:
            await ctx.send("Wrong use! Please use this:"
                           "```!guildfamily set <url>```")
        else:
            from utils import get_confirmation, ReturnCodes

            confirmation_message = await ctx.send("You are about to change the url of this guild.\n"
                                                  "Do you want to continue?")

            confirmation = await get_confirmation(confirmation_message, ctx.author, client)

            if confirmation == ReturnCodes.SUCCESS:
                set_process = set_family(ctx.guild.id, args[1])
                if set_process == ReturnCodes.SUCCESS:
                    guild_family_file = open(f"data/guild_familys/{ctx.guild.id}.txt", "r")
                    family = guild_family_file.read()
                    guild_family_file.close()
                    await ctx.send(f"The default URL of the guild has been changed to```{family}```")
                elif set_process == ReturnCodes.OTHER_ERROR:
                    await ctx.send("An unknown error has occurred.\n"
                                   "If that happens every time, contact our support.")
                elif set_process == ReturnCodes.VARIABLE_INVAILED:
                    await ctx.send("You didn't use `%ARTICLE%` in the url.")
                elif set_process == ReturnCodes.NO_CHANGES:
                    await ctx.send("There are no changes in the url.")
            elif confirmation == ReturnCodes.CANCELLED:
                await ctx.send("The process was successfully cancelled.")

            elif confirmation == ReturnCodes.TIMEOUT_ERROR:
                await confirmation.delete()

            elif confirmation == ReturnCodes.OTHER_ERROR:
                await ctx.send("An unknown error has occurred.\n"
                               "If that happens every time, contact our support.")
    elif args[0] == "clear" or args[0] == "delete":
        from utils import get_confirmation, ReturnCodes

        confirmation_message = await ctx.send("You are about to clear the url of this guild.\n"
                                              "Do you want to continue?")

        confirmation = await get_confirmation(confirmation_message, ctx.author, client)

        if confirmation == ReturnCodes.SUCCESS:
            clear_process = clear_family(ctx.guild.id)

            if clear_process == ReturnCodes.SUCCESS:
                await ctx.send("The url of this guild has been successfully reset.")

            elif clear_process == ReturnCodes.NOT_FOUND:
                await ctx.send("This guild has no default url.")

        elif confirmation == ReturnCodes.CANCELLED:
            await ctx.send("The process was successfully cancelled.")

        elif confirmation == ReturnCodes.TIMEOUT_ERROR:
            await confirmation.delete()

        elif confirmation == ReturnCodes.OTHER_ERROR:
            await ctx.send("An unknown error has occurred.\n"
                           "If that happens every time, contact our support.")


def set_family(guild_id, family_url):
    from utils import ReturnCodes

    try:
        from utils import get_family_template, ReturnCodes
        template_search_process = get_family_template(family_url)
        if template_search_process != ReturnCodes.NOT_FOUND:
            family_url = template_search_process

        if "%article%" not in family_url.lower():
            return ReturnCodes.VARIABLE_INVAILED

        import os
        if os.path.isfile(f"data/guild_familys/{str(guild_id)}.txt"):
            guild_family_file = open(f"data/guild_familys/{str(guild_id)}.txt", "r")
            if family_url == guild_family_file.read():
                guild_family_file.close()
                return ReturnCodes.NO_CHANGES
            guild_family_file.close()

        guild_family_file = open(f"data/guild_familys/{str(guild_id)}.txt", "w")
        guild_family_file.write(family_url)
        guild_family_file.close()

        return ReturnCodes.SUCCESS
    except:
        return ReturnCodes.OTHER_ERROR


def clear_family(guild_id):
    from utils import ReturnCodes

    import os
    if os.path.isfile(f"data/guild_familys/{str(guild_id)}.txt"):
        os.remove(f"data/guild_familys/{str(guild_id)}.txt")
        return ReturnCodes.SUCCESS
    else:
        return ReturnCodes.NOT_FOUND


def get_family(guild_id):
    from utils import ReturnCodes
    import os

    if os.path.isfile(f"data/guild_familys/{str(guild_id)}.txt"):
        guild_family_file = open(f"data/guild_familys/{str(guild_id)}.txt", "r")
        guild_family = guild_family_file.read()
        guild_family_file.close()
        return guild_family
    else:
        return ReturnCodes.NOT_FOUND
