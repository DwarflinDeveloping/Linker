async def manage_request(ctx, *args, client):
    args = [arg.lower() for arg in args]
    if len(args) == 0:
        from commands.help import send_userfamily_help
        await send_userfamily_help(ctx)
        return

    if args[0] == "get" or args[0] == "query":
        from utils import ReturnCodes

        get_family_process = get_family(ctx.author.id)
        if get_family_process == ReturnCodes.NOT_FOUND:
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_message="You have no Default URL.",
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
                    embed_message=f"Your Default URL is:```{get_family_process}```",
                    user=ctx.author,
                    colour=Colour.blue()
                )
            )

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
                    "You are about to change your Default URL.\n"
                    "Do you want to continue?",
                    user=ctx.author,
                    colour=Colour.blue()
                )
            )

            confirmation = await get_confirmation(confirmation_message, ctx.author, client)
            if confirmation == ReturnCodes.SUCCESS:
                set_process = set_family(ctx.author.id, args[1])
                if set_process == ReturnCodes.SUCCESS:
                    user_family_file = open(f"data/guild_familys/{ctx.guild.id}.txt", "r")
                    await ctx.send(
                        embed=create_custom_embed(
                            embed_title="Success",
                            embed_message=f"Your Default URL has been changed to```{user_family_file.read()}```",
                            user=ctx.author,
                            colour=Colour.dark_green()
                        )
                    )
                    user_family_file.close()
                elif set_process == ReturnCodes.VARIABLE_INVAILED:
                    await ctx.send(
                        embed=create_custom_embed(
                            embed_message="You didn't use `%ARTICLE%` in the Default URL.",
                            user=ctx.author,
                            colour=Colour.dark_red()
                        )
                    )
                elif set_process == ReturnCodes.NO_CHANGES:
                    await ctx.send(
                        embed=create_custom_embed(
                            embed_message="There are no changes in the Default URL.",
                            user=ctx.author,
                            colour=Colour.dark_red()
                        )
                    )
                elif set_process == ReturnCodes.OTHER_ERROR:
                    from embeds import handle_error
                    await ctx.send(embed=handle_error(set_process, ctx.author))
            elif confirmation == ReturnCodes.CANCELLED:
                await confirmation_message.delete()

            elif confirmation == ReturnCodes.TIMEOUT_ERROR:
                await confirmation.delete()

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
                "You are about to clear your Default URL.\n"
                "Do you want to continue?",
                user=ctx.author,
                colour=Colour.blue()
            )
        )

        confirmation = await get_confirmation(confirmation_message, ctx.author, client)

        if confirmation == ReturnCodes.SUCCESS:
            clear_process = clear_family(ctx.author.id)

            if clear_process == ReturnCodes.SUCCESS:
                await ctx.send(
                    embed=create_custom_embed(
                        embed_title="Success",
                        embed_message=f"Your Default URL has been successfully reset.",
                        user=ctx.author,
                        colour=Colour.dark_green()
                    )
                )

            elif clear_process == ReturnCodes.NOT_FOUND:
                await ctx.send(
                    embed=create_custom_embed(
                        embed_message="You have no Default URL.",
                        user=ctx.author,
                        colour=Colour.dark_red()
                    )
                )

        elif confirmation == ReturnCodes.CANCELLED or confirmation == ReturnCodes.TIMEOUT_ERROR:
            await confirmation_message.delete()

        elif confirmation == ReturnCodes.OTHER_ERROR:
            from embeds import handle_error
            await ctx.send(embed=handle_error(confirmation, ctx.author))
    else:
        from commands.help import send_userfamily_help
        await send_userfamily_help(ctx)


def set_family(user_id, family_url):
    from utils import get_family_template, ReturnCodes
    import os

    template_search_process = get_family_template(family_url)
    if template_search_process != ReturnCodes.NOT_FOUND:
        family_url = template_search_process

    if "%article%" not in family_url.lower():
        return ReturnCodes.VARIABLE_INVAILED
    if os.path.isfile(f"data/user_familys/{str(user_id)}.txt"):
        user_family_file = open(f"data/user_familys/{str(user_id)}.txt", "r")
        if family_url == user_family_file.read():
            user_family_file.close()
            return ReturnCodes.NO_CHANGES
        user_family_file.close()

    try:
        user_family_file = open(f"data/user_familys/{str(user_id)}.txt", "w")
        user_family_file.write(family_url)
        user_family_file.close()
        return ReturnCodes.SUCCESS
    except:
        return ReturnCodes.OTHER_ERROR


def clear_family(user_id):
    from utils import ReturnCodes

    import os
    if os.path.isfile(f"data/user_familys/{str(user_id)}.txt"):
        os.remove(f"data/user_familys/{str(user_id)}.txt")
        return ReturnCodes.SUCCESS
    else:
        return ReturnCodes.NOT_FOUND


def get_family(user_id):
    from utils import ReturnCodes
    import os

    if os.path.isfile(f"data/user_familys/{str(user_id)}.txt"):
        user_family_file = open(f"data/user_familys/{str(user_id)}.txt", "r")
        user_family = user_family_file.read()
        user_family_file.close()
        return user_family
    else:
        return ReturnCodes.NOT_FOUND
