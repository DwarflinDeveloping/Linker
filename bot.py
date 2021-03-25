import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="%", intents=discord.Intents.all())
bot.help_command = None


@bot.listen("on_message")
async def send_link(message):
    if "{" not in message.content or message.author.bot:
        return
    from search import manage_search
    link_content = manage_search(message)
    if len(link_content) > 2000:
        await message.channel.send("You included too many links in this message!")
        return
    await message.channel.send(link_content)


@bot.command()
async def help(ctx, *args):
    from help import manage_request
    await manage_request(ctx, *args)


@bot.command()
async def admin(ctx, *args):
    from admincmds import manage_request
    await manage_request(ctx, *args)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                        name="%help"))
    print("Logged on as", bot.user)


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
