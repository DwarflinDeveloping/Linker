async def manage_request(ctx, *args, client):
    args = [arg.lower() for arg in args]
    if len(args) == 0:
        from commands.help import send_op_command_help
        await send_op_command_help(ctx)

    elif args[0] == "list" or args[0] == "get":
        get_process = get_operators()
        from utils import ReturnCodes
        if get_process == ReturnCodes.NOT_FOUND:
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_message="There are no system operators.",
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
                    embed_title="System operators",
                    embed_message=f"The system operators are```{custom_words}```",
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
                "You are about to clear the system operators.\n"
                "Do you want to continue?",
                user=ctx.author,
                colour=Colour.blue()
            )
        )
        confirmation = await get_confirmation(confirmation_message, ctx.author, client)

        if confirmation == ReturnCodes.SUCCESS:
            clear_process = clear_operators()
            if clear_process == ReturnCodes.NOT_FOUND:
                from embeds import create_custom_embed
                await ctx.send(
                    embed=create_custom_embed(
                        embed_message="There are no system operators.",
                        user=ctx.author
                    )
                )
            elif clear_process == ReturnCodes.OTHER_ERROR:
                from embeds import handle_error
                await ctx.send(embed=handle_error(ReturnCodes.OTHER_ERROR, ctx.author))
            elif clear_process == ReturnCodes.SUCCESS:
                from embeds import create_custom_embed
                from discord import Colour
                await ctx.send(
                    embed=create_custom_embed(
                        embed_title="Successfully completed",
                        embed_message="The system operators have been succesfully cleared.",
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

    if len(args) != 2:
        from commands.help import send_op_command_help
        await send_op_command_help(ctx)

    elif args[0] == "remove" or args[0] == "rem":
        from utils import ReturnCodes, get_confirmation
        from embeds import create_custom_embed
        from discord import Colour

        confirmation_message = await ctx.send(
            embed=create_custom_embed(
                embed_title=
                "Confirmation",
                embed_message=
                "You are about to change the system operators.\n"
                "Do you want to continue?",
                user=ctx.author,
                colour=Colour.blue()
            )
        )

        confirmation = await get_confirmation(confirmation_message, ctx.author, client)

        if confirmation == ReturnCodes.SUCCESS:
            remove_process = remove_operator(int(args[1]))
            from utils import ReturnCodes
            if remove_process == ReturnCodes.SUCCESS:
                from embeds import create_custom_embed
                from discord import Colour
                await ctx.send(
                    embed=create_custom_embed(
                        embed_title="Successfully completed",
                        embed_message=f"Operator rights successfully removed from user `{args[1]}`.",
                        user=ctx.author,
                        colour=Colour.green()
                    )
                )
            elif remove_process == ReturnCodes.NOT_FOUND:
                from embeds import create_custom_embed
                from discord import Colour
                await ctx.send(
                    embed=create_custom_embed(
                        embed_message="There are no system operators.",
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
        try:
            int(args[1])
        except ValueError:
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_message=f"An ID must consist exclusively of numbers.",
                    user=ctx.author,
                    colour=Colour.dark_red()
                )
            )
            return

        add_process = add_operator(int(args[1]))
        from utils import ReturnCodes
        if add_process == ReturnCodes.SUCCESS:
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_title="Successfully completed",
                    embed_message=f"Operator rights successfully added to user `{args[1]}`.",
                    user=ctx.author,
                    colour=Colour.green()
                )
            )
        if add_process == ReturnCodes.NO_CHANGES:
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_message=f"The user `{args[1]}` allready has operator rights.",
                    user=ctx.author,
                    colour=Colour.dark_red()
                )
            )

    else:
        # TODO Syntax Error
        pass


def add_operator(operator_id):
    import json
    import os
    from utils import ReturnCodes
    operator_id = str(operator_id)
    if os.path.isfile(f"data/rights.json"):
        with open(f"data/rights.json", "r") as json_file:
            custom_words = json.load(json_file)
        if operator_id in custom_words and custom_words[operator_id] == "operator":
            return ReturnCodes.NO_CHANGES
        custom_words[operator_id] = "operator"
        json_file.close()
    else:
        custom_words = {operator_id: "operator"}
    with open(f"data/rights.json", "w") as json_file:
        json_file.write(json.dumps(custom_words, indent=4))
    json_file.close()
    return ReturnCodes.SUCCESS


def remove_operator(operator_id):
    import json
    import os
    from utils import ReturnCodes

    if not os.path.isfile(f"data/rights.json"):
        return ReturnCodes.NOT_FOUND

    with open(f"data/rights.json", "r") as json_file:
        custom_words = json.load(json_file)
    if str(operator_id) not in custom_words:
        return ReturnCodes.NOT_FOUND
    del custom_words[str(operator_id)]
    json_file.close()

    with open(f"data/rights.json", "w") as json_file:
        json_file.write(json.dumps(custom_words, indent=4))
    json_file.close()

    return ReturnCodes.SUCCESS


def get_operators():
    import os
    from utils import ReturnCodes

    file_path = "data/rights.json"
    if not os.path.isfile(file_path):
        return ReturnCodes.NOT_FOUND

    custom_words_file = open(file_path)
    import json
    custom_words_json = json.loads(custom_words_file.read())
    custom_words_file.close()
    custom_words_keys = custom_words_json.keys()
    custom_words = []

    if len(custom_words_keys) == 0:
        return ReturnCodes.NOT_FOUND

    for key in custom_words_keys:
        if "operator" in custom_words_json[key]:
            custom_words += [key]

    return custom_words


def clear_operators():
    import os
    from utils import ReturnCodes

    file_path = "data/rights.json"

    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
            return ReturnCodes.SUCCESS
        except:
            return ReturnCodes.OTHER_ERROR
    else:
        return ReturnCodes.NOT_FOUND
