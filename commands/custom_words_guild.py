async def manage_request(ctx, *args, client):
    args = [arg.lower() for arg in args]
    if len(args) == 0:
        from commands.help import send_guildwords_help
        await send_guildwords_help(ctx)

    elif args[0] == "list" or args[0] == "get":
        get_process = get_custom_words_by_guild(ctx.guild.id)
        from utils import ReturnCodes
        if get_process == ReturnCodes.NOT_FOUND:
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_message="This guild has no custom words.",
                    user=ctx.author,
                    colour=Colour.dark_red()
                )
            )
        else:
            custom_words = ""
            for verify_message in get_process:
                custom_words += f"• {verify_message.replace('=', ' = ')}\n"
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_title="Custom words",
                    embed_message=f"The custom words of this guild are:```{custom_words}```",
                    user=ctx.author,
                    colour=Colour.blue()
                )
            )

    elif args[0] == "clear":
        from embeds import create_custom_embed
        from discord import Colour
        from utils import ReturnCodes, get_confirmation
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
            clear_process = clear_custom_words_by_guild(ctx.guild.id)
            if clear_process == ReturnCodes.NOT_FOUND:
                from embeds import create_custom_embed
                await ctx.send(embed=create_custom_embed("This guild has no custom words.", ctx.author))
            elif clear_process == ReturnCodes.OTHER_ERROR:
                from embeds import handle_error
                await ctx.send(embed=handle_error(ReturnCodes.OTHER_ERROR, ctx.author))
            elif clear_process == ReturnCodes.SUCCESS:
                from embeds import create_custom_embed
                from discord import Colour
                await ctx.send(
                    embed=create_custom_embed(
                        embed_title="Successfully completed",
                        embed_message="The guilds custom words succesfully cleared.",
                        user=ctx.author,
                        colour=Colour.green()
                    )
                )
        elif confirmation == ReturnCodes.CANCELLED:
            await confirmation_message.delete()

        elif confirmation == ReturnCodes.TIMEOUT_ERROR:
            await confirmation_message.delete()

        elif confirmation == ReturnCodes.OTHER_ERROR:
            from embeds import handle_error
            await ctx.send(handle_error(confirmation, ctx.author))

    elif args[0] == "remove" or args[0] == "rem":
        from utils import ReturnCodes, get_confirmation
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
            remove_process = remove_custom_guild_word(ctx.guild.id, args[1])
            from utils import ReturnCodes
            if remove_process == ReturnCodes.SUCCESS:
                from embeds import create_custom_embed
                from discord import Colour
                await ctx.send(
                    embed=create_custom_embed(
                        embed_title="Successfully completed",
                        embed_message=f"The word `{args[1]}` was successfully removed.",
                        user=ctx.author,
                        colour=Colour.green()
                    )
                )
            elif remove_process == ReturnCodes.NOT_FOUND:
                from embeds import create_custom_embed
                from discord import Colour
                await ctx.send(
                    embed=create_custom_embed(
                        embed_message="This guild doesn't has this custom word.",
                        user=ctx.author,
                        colour=Colour.dark_red()
                    )
                )

        elif confirmation == ReturnCodes.CANCELLED:
            await confirmation_message.delete()

        elif confirmation == ReturnCodes.TIMEOUT_ERROR:
            await confirmation_message.delete()

        elif confirmation == ReturnCodes.OTHER_ERROR:
            from embeds import handle_error
            await ctx.send(embed=handle_error(confirmation, ctx.author))

    elif args[0] == "add":
        add_process = create_custom_guild_word(ctx.guild.id, args[1], args[2])
        from utils import ReturnCodes
        if add_process == ReturnCodes.SUCCESS:
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_title="Successfully completed",
                    embed_message=f"The word `{args[1]}` was successfully set to the url `{args[2]}`.",
                    user=ctx.author,
                    colour=Colour.green()
                )
            )
        if add_process == ReturnCodes.NO_CHANGES:
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_message=f"The word `{args[1]}` is allready set to `{args[2]}`.",
                    user=ctx.author,
                    colour=Colour.dark_red()
                )
            )

    else:
        from commands.help import send_guildwords_help
        await send_guildwords_help(ctx)


def create_custom_guild_word(guild_id, custom_word, url):
    import json
    import os
    from utils import ReturnCodes

    if os.path.isfile(f"data/custom_words/guilds/{guild_id}.json"):
        with open(f"data/custom_words/guilds/{guild_id}.json", "r") as json_file:
            custom_words = json.load(json_file)
        if custom_word in custom_words and custom_words[custom_word] == url:
            return ReturnCodes.NO_CHANGES
        custom_words[custom_word] = url
        json_file.close()
    else:
        custom_words = {custom_word: url}
    with open(f"data/custom_words/guilds/{guild_id}.json", "w") as json_file:
        json_file.write(json.dumps(custom_words, indent=4))
    json_file.close()

    return ReturnCodes.SUCCESS


def remove_custom_guild_word(guild_id, custom_word):
    import json
    import os
    from utils import ReturnCodes

    if not os.path.isfile(f"data/custom_words/guilds/{guild_id}.json"):
        return ReturnCodes.NOT_FOUND

    with open(f"data/custom_words/guilds/{guild_id}.json", "r") as json_file:
        custom_words = json.load(json_file)
    if custom_word not in custom_words:
        return ReturnCodes.NOT_FOUND
    del custom_words[custom_word]
    json_file.close()

    with open(f"data/custom_words/guilds/{guild_id}.json", "w") as json_file:
        json_file.write(json.dumps(custom_words, indent=4))
    json_file.close()

    return ReturnCodes.SUCCESS


def get_custom_words_by_guild(guild_id):
    import os
    from utils import ReturnCodes
    if not os.path.isfile(f"data/custom_words/guilds/{guild_id}.json"):
        return ReturnCodes.NOT_FOUND
    custom_words_file = open(f"data/custom_words/guilds/{guild_id}.json")
    import json
    custom_words_json = json.loads(custom_words_file.read())
    custom_words_file.close()
    custom_words_keys = custom_words_json.keys()
    custom_words = []

    if len(custom_words_keys) == 0:
        return ReturnCodes.NOT_FOUND

    for key in custom_words_keys:
        custom_words += [f"{key}={custom_words_json[key]}"]

    return custom_words


def clear_custom_words_by_guild(guild_id):
    import os
    from utils import ReturnCodes

    file_path = f"data/custom_words/guilds/{guild_id}.json"

    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
            return ReturnCodes.SUCCESS
        except:
            return ReturnCodes.OTHER_ERROR
    else:
        return ReturnCodes.NOT_FOUND
