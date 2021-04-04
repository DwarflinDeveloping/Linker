async def manage_request(ctx, *args, client):
    args = [arg.lower() for arg in args]
    if len(args) == 0:
        from commands.help import send_guildfamily_help
        await send_guildfamily_help(ctx)
        return
    elif args[0] == "get" or args[0] == "query":
        from utils import ReturnCodes

        get_family_process = get_family(ctx.guild.id)
        if get_family_process == ReturnCodes.NOT_FOUND:
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_message=f"This guild has no Default URL.",
                    user=ctx.author,
                    colour=Colour.dark_red()
                )
            )
        else:
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_title="Default URL",
                    embed_message=f"The Default URL of this guild is```{get_family_process}```",
                    user=ctx.author,
                    colour=Colour.blue()
                )
            )
    elif not ctx.channel.permissions_for(ctx.author).manage_messages:
        from embeds import create_custom_embed
        from discord import Colour
        await ctx.send(
            embed=create_custom_embed(
                embed_message=f"You are not permitted to change the guilds Default URL!",
                user=ctx.author,
                colour=Colour.dark_red()
            )
        )
        return
    elif args[0] == "set":
        if len(args) != 2:
            from commands.help import send_userfamily_help
            await send_userfamily_help(ctx)
        else:
            from utils import get_confirmation, ReturnCodes
            from embeds import create_custom_embed
            from discord import Colour
            confirmation_message = await ctx.send(
                embed=create_custom_embed(
                    embed_title=
                    "Confirmation",
                    embed_message=
                    "You are about to change the url of this guild.\n"
                    "Do you want to continue?",
                    user=ctx.author,
                    colour=Colour.blue()
                )
            )

            confirmation = await get_confirmation(confirmation_message, ctx.author, client)

            if confirmation == ReturnCodes.SUCCESS:
                set_process = set_family(ctx.guild.id, args[1])
                if set_process == ReturnCodes.SUCCESS:
                    guild_family_file = open(f"data/guild_familys/{ctx.guild.id}.txt", "r")

                    await ctx.send(
                        embed=create_custom_embed(
                            embed_title="Success",
                            embed_message=f"The Default URL of the guild has been changed to```{guild_family_file.read()}```",
                            user=ctx.author,
                            colour=Colour.dark_green()
                        )
                    )

                    guild_family_file.close()

                elif set_process == ReturnCodes.OTHER_ERROR:
                    from embeds import handle_error
                    await ctx.send(embed=handle_error(confirmation, ctx.author))
                elif set_process == ReturnCodes.VARIABLE_INVAILED:
                    await ctx.send(
                        embed=create_custom_embed(
                            embed_message="You didn't use `%ARTICLE%` in the url.",
                            user=ctx.author,
                            colour=Colour.dark_red()
                        )
                    )
                elif set_process == ReturnCodes.NO_CHANGES:
                    await ctx.send(
                        embed=create_custom_embed(
                            embed_message="There are no changes in the url.",
                            user=ctx.author,
                            colour=Colour.dark_red()
                        )
                    )
            elif confirmation == ReturnCodes.CANCELLED or confirmation == ReturnCodes.TIMEOUT_ERROR:
                await confirmation_message.delete()

            elif confirmation == ReturnCodes.OTHER_ERROR:
                from embeds import handle_error
                await ctx.send(embed=handle_error(confirmation, ctx.author))
    elif args[0] == "clear" or args[0] == "delete":
        from utils import get_confirmation, ReturnCodes
        from embeds import create_custom_embed
        from discord import Colour
        confirmation_message = await ctx.send(
            embed=create_custom_embed(
                embed_title=
                "Confirmation",
                embed_message=
                "You are about to clear the guilds Default URL.\n"
                "Do you want to continue?",
                user=ctx.author,
                colour=Colour.blue()
            )
        )

        confirmation = await get_confirmation(confirmation_message, ctx.author, client)

        if confirmation == ReturnCodes.SUCCESS:
            clear_process = clear_family(ctx.guild.id)

            if clear_process == ReturnCodes.SUCCESS:
                await ctx.send(
                    embed=create_custom_embed(
                        embed_title="Success",
                        embed_message="The Default URL of this guild has been successfully reset.",
                        user=ctx.author,
                        colour=Colour.dark_green()
                    )
                )

            elif clear_process == ReturnCodes.NOT_FOUND:
                await ctx.send(
                    embed=create_custom_embed(
                        embed_message="This guild has no Default URL.",
                        user=ctx.author,
                        colour=Colour.dark_red()
                    )
                )

        elif confirmation == ReturnCodes.CANCELLED or ReturnCodes.TIMEOUT_ERROR:
            await confirmation_message

        elif confirmation == ReturnCodes.OTHER_ERROR:
            from embeds import handle_error
            await ctx.send(embed=handle_error(confirmation, ctx.author))


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

