import discord
import re

from discord.ext import commands

bot = commands.Bot(command_prefix="%")

links = ""
trusted_members = []
administrators = [784473264755834880]


@bot.listen("on_message")
async def send_link(message):
    global links
    if "[[" not in message.content or message.author.bot:
        return

    items = re.findall("\\[\\[[^\\]]*\\]\\]", message.content)
    searches = []
    for item in items:
        item = re.sub('[\\[\\]]', '', item)
        item = re.sub('\\s', '_', item)
        searches += [item]

    for search in searches:
        if ":" in search:
            search_family = search.split(":")[0].replace("$", "")
            if search_family == "mc":
                search_family = "minecraft-de.gamepedia.com"
            elif search_family == "mcen":
                search_family = "minecraft-en.gamepedia.com"
            elif search_family.startswith("w-"):
                wikipedia_family = search.split(":")[0].split("w-")[1]
                if len(wikipedia_family) != 2:
                    return
                search_family = f"{wikipedia_family}.wikipedia.org/wiki"
            elif search_family.startswith("gp-"):
                gamepedia_family = search.split(":")[0].split("gp-")[1]
                search_family = f"{gamepedia_family}.gamepedia.com"
            elif search_family.startswith("f-"):
                gamepedia_family = search.split(":")[0].split("f-")[1]
                search_family = f"{gamepedia_family}.fandom.com"
            elif search.split(":")[0] == "mctw":
                search_family = "technik-de.gamepedia.com"
            else:
                search_family = search.split(":")[0]
            search_request = search.split(":")[1]
            search_url = f"https://{search_family}/{search_request}"
        else:
            import os
            user_has_custom_family = os.path.isfile(f"data/user_familys/{str(message.author.id)}.txt")
            search_request = search
            if not user_has_custom_family:
                guild_family_file = open(f"data/guild_familys/{str(message.guild.id)}.txt", "r")
                search_url = guild_family_file.read().replace("%ARTICLE%", search_request)
                guild_family_file.close()
            else:
                guild_family_file = open(f"data/user_familys/{str(message.author.id)}.txt", "r")
                search_url = guild_family_file.read().replace("%ARTICLE%", search_request)
                guild_family_file.close()
        if search.startswith("$"):
            search_url = search_url.replace("$", "")
            search_text = search_url
        else:
            search_text = f"<{search_url}>"
        links += search_text + "\n"
    await message.channel.send(links)
    links = ""
    await bot.process_commands(message)


@bot.command()
async def admin(ctx, *args):
    if args[0] == "guildfam":
        if len(args) != 2:
            # TODO Syntax Error
            await ctx.send("SYNTAX ERROR!")
        else:
            from guild_family import get_family
            from utils import ReturnCodes

            get_family_process = get_family(ctx.guild.id)
            if get_family_process == ReturnCodes.NOT_FOUND:
                await ctx.send("This guild has no default url.")

            else:
                await ctx.send(f"The default url of this guild is:```{get_family_process}```")
    if args[0] == "userfam":
        if len(args) != 2:
            # TODO Syntax Error
            await ctx.send("SYNTAX ERROR!")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                        name="%troubble"))
    print("Logged on as", bot.user)


@bot.command()
async def troubble(ctx, *args):
    if len(args) == 0:
        await ctx.send(
            "**help articles:**\n"
            "`%troubble changefamily`")
    elif args[0] == "changefamily":
        # TODO Link
        await ctx.send("To change the default url of a guild you need the \"manage_messages\" permission.\n\n"
                       "Still in trouble? LINK")
        return
    else:
        await ctx.send("I could not find this article.")


@bot.command()
async def op(ctx, *args):
    if ctx.author.id not in administrators:
        await ctx.send("You are not allowed to change operators rights.")
        return
    global trusted_members
    if args[0] == "get" or args[0] == "query":
        operators = ""
        for operator in trusted_members:
            operators += f"{operator}\n"
        await ctx.send(f"```{operators}```")
        return
    if args[0] == "rem" or args[0] == "remove":
        if len(args) != 2:
            await ctx.send("Wrong use! Please use this:"
                           f"```%op {args[0]} <user id>```")
            return
        if args[1] not in trusted_members:
            await ctx.send(f"The user `{args[1]}` has no operator rights.")
            return
        trusted_members.remove(args[1])
        await ctx.send(f"The operator rights of this user have been removed:```{args[1]}```")
        return
    if args[0] == "add":
        if len(args) != 2:
            await ctx.send("Wrong use! Please use this:"
                           f"```%op {args[0]} <user id>```")
            return
        if args[1] in trusted_members:
            await ctx.send(f"The user `{args[1]}` already has operator rights.")
            return
        trusted_members += [args[1]]
        await ctx.send(f"The operator rights have been added to this user:```{args[1]}```")
        return


@bot.command()
async def guildfamily(ctx, *args):
    if args[0] == "get" or args[0] == "query":
        from utils import ReturnCodes
        from guild_family import get_family

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

            confirmation = await get_confirmation(confirmation_message, ctx.author, bot)

            if confirmation == ReturnCodes.SUCCESS:
                from guild_family import set_family
                set_process = set_family(ctx.guild.id, args[1])
                if set_process == ReturnCodes.SUCCESS:
                    await ctx.send(f"The default URL of the guild has been changed to```{args[1]}```")
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

        confirmation_message = await ctx.send("You are about to clear the url of this guild.\n"
                                              "Do you want to continue?")

        confirmation = await get_confirmation(confirmation_message, ctx.author, bot)

        if confirmation == ReturnCodes.SUCCESS:
            from guild_family import clear_family
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


@bot.command()
async def userfamily(ctx, *args):
    if args[0] == "get" or args[0] == "query":
        from utils import ReturnCodes
        from user_family import get_family

        get_family_process = get_family(ctx.guild.id)
        if get_family_process == ReturnCodes.NOT_FOUND:
            await ctx.send("You have no default url.")
        else:
            await ctx.send(f"Your default url is:```{get_family_process}```")
    elif args[0] == "set":
        if len(args) != 2:
            await ctx.send("Wrong use! Please use this:"
                           "```!guildfamily set <url>```")
        else:
            from utils import get_confirmation, ReturnCodes

            confirmation_message = await ctx.send("You are about to change the url of this guild.\n"
                                                  "Do you want to continue?")

            confirmation = await get_confirmation(confirmation_message, ctx.author, bot)

            if confirmation == ReturnCodes.SUCCESS:
                from user_family import set_family
                set_process = set_family(ctx.author.id, args[1])
                if set_process == ReturnCodes.SUCCESS:
                    await ctx.send(f"Your default URL has been changed to```{args[1]}```")
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

        confirmation = await get_confirmation(confirmation_message, ctx.author, bot)

        if confirmation == ReturnCodes.SUCCESS:
            from user_family import clear_family
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


bot.run("TOKEN")
