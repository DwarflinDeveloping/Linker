async def manage_request(ctx, *args, client):
    if len(args) == 0:
        from commands.help import send_userfamily_help
        await send_userfamily_help(ctx, *args)
        return
    args = [arg.lower() for arg in args]
    if args[0] == "get" or args[0] == "query":
        from utils import ReturnCodes

        get_family_process = get_family(ctx.author.id)
        if get_family_process == ReturnCodes.NOT_FOUND:
            await ctx.send("You have no default url.")
        else:
            await ctx.send(f"Your default url is:```{get_family_process}```")
    elif args[0] == "set":
        if len(args) != 2:
            await ctx.send("Wrong use! Please use this:"
                           "```%userfamily set <url>```")
        else:
            from utils import get_confirmation, ReturnCodes

            confirmation_message = await ctx.send("You are about to change your default url.\n"
                                                  "Do you want to continue?")

            confirmation = await get_confirmation(confirmation_message, ctx.author, client)

            if confirmation == ReturnCodes.SUCCESS:
                set_process = set_family(ctx.author.id, args[1])
                if set_process == ReturnCodes.SUCCESS:
                    await ctx.send(f"Your default URL has been changed to```{args[1]}```")
                elif set_process == ReturnCodes.VARIABLE_INVAILED:
                    await ctx.send("You didn't use `%ARTICLE%` in the url.")
                elif set_process == ReturnCodes.NO_CHANGES:
                    await ctx.send("There are no changes in the url.")
                elif set_process == ReturnCodes.OTHER_ERROR:
                    await ctx.send("An unknown error has occurred.\n"
                                   "If that happens every time, contact our support.")
            elif confirmation == ReturnCodes.CANCELLED:
                await ctx.send("The process was successfully cancelled.")

            elif confirmation == ReturnCodes.TIMEOUT_ERROR:
                await confirmation.delete()

            elif confirmation == ReturnCodes.OTHER_ERROR:
                await ctx.send("An unknown error has occurred.\n"
                               "If that happens every time, contact our support.")
    elif args[0] == "clear" or args[0] == "delete":
        from utils import get_confirmation, ReturnCodes

        confirmation_message = await ctx.send("You are about to clear your default url.\n"
                                              "Do you want to continue?")

        confirmation = await get_confirmation(confirmation_message, ctx.author, client)

        if confirmation == ReturnCodes.SUCCESS:
            clear_process = clear_family(ctx.author.id)

            if clear_process == ReturnCodes.SUCCESS:
                await ctx.send("Your default url has been successfully reset.")

            elif clear_process == ReturnCodes.NOT_FOUND:
                await ctx.send("You have no default url.")

        elif confirmation == ReturnCodes.CANCELLED:
            await ctx.send("The process was successfully cancelled.")

        elif confirmation == ReturnCodes.TIMEOUT_ERROR:
            await confirmation.delete()

        elif confirmation == ReturnCodes.OTHER_ERROR:
            await ctx.send("An unknown error has occurred.\n"
                           "If that happens every time, contact our support.")


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
