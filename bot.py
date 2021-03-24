import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="%")


@bot.listen("on_message")
async def send_link(message):
    if "[[" not in message.content or message.author.bot:
        return
    from search import manage_search
    link_content = manage_search(message)
    await message.channel.send(link_content)


@bot.command()
async def admin(ctx, *args):
    from admincmds import manage_request
    await manage_request(ctx, *args)


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
    from manage_op import manage_request
    await manage_request(ctx, *args)


@bot.command()
async def guildfamily(ctx, *args):
    from guild_family import manage_request
    await manage_request(ctx, *args, client=bot)


@bot.command()
async def userfamily(ctx, *args):
    from user_family import manage_request
    await manage_request(ctx, *args, client=bot)


bot.run("TOKEN")
