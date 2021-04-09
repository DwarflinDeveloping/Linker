#!/usr/bin/python3

import discord
from discord.ext import commands as cmds

import os

bot = cmds.Bot(command_prefix="%", intents=discord.Intents.all())
bot.help_command = None


def make_directories():
    from os.path import isdir
    if not isdir("data"):
        os.mkdir("data")
    if not isdir("data/custom_words"):
        os.mkdir("data/custom_words")
    if not isdir("data/guild_familys"):
        os.mkdir("data/guild_familys")
    if not isdir("data/user_familys"):
        os.mkdir("data/user_familys")


@bot.listen("on_raw_reaction_add")
async def delete_awnser(payload):
    from commands.admincmds import paused
    if paused:
        return
    if payload.emoji.name != "🗑️️":
        return
    guild = discord.utils.get(bot.guilds, id=payload.guild_id)
    channel = discord.utils.get(await guild.fetch_channels(), id=payload.channel_id)
    message = channel.fetch_message(payload.message_id)
    if message.author.id != bot.user.id:
        return
    from embeds import create_custom_embed
    from discord import Colour
    await channel.send(
        embed=create_custom_embed(
            embed_title="Successfully completed",
            embed_message=f"This message will be deleted in 5 seconds. To cancel this process, react with a \"❌\".",
            user=message.author,
            colour=Colour.green()
        )
    )
    from utils import get_confirmation, ReturnCodes

    confirmation = await get_confirmation(message, message.author, bot)
    if confirmation == ReturnCodes.SUCCESS:
        await message.delete()
    elif confirmation == ReturnCodes.CANCELLED:
        await message.delete()

    elif confirmation == ReturnCodes.TIMEOUT_ERROR:
        await message.delete()

    elif confirmation == ReturnCodes.OTHER_ERROR:
        from embeds import handle_error
        await message.channel.send(embed=handle_error(confirmation, message.author))


@bot.listen("on_message")
async def send_link(message):
    from commands.admincmds import paused
    if paused:
        return
    if "{" not in message.content or message.author.bot:
        return
    from search import manage_search
    links = manage_search(message)
    if len(links[0]) > 2000:
        await message.channel.send("You included too many links in this message!")
        return
    if links[1] is True:
        await message.channel.send(
            links[0] +
            "\nYou have not yet set a default URL!\n"
            "For help, type `%help default url`."
        )
    else:
        await message.channel.send(links[0])


@bot.command()
async def help(ctx, *args):
    from commands.admincmds import paused
    if paused:
        return
    from commands import help
    await help.manage_request(ctx, *args)


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="%help"
        )
    )
    print("Logged on as", bot.user)


@bot.command()
async def userwords(ctx, *args):
    from commands.admincmds import paused
    if paused:
        return
    from commands.custom_words_user import manage_request
    await manage_request(ctx, *args, client=bot)


@bot.command()
async def op(ctx, *args):
    from commands.admincmds import paused
    if paused:
        return
    from commands.manage_operators import manage_request
    await manage_request(ctx, *args, client=bot)


@bot.command()
async def guildwords(ctx, *args):
    from commands.admincmds import paused
    if paused:
        return
    from commands.custom_words_guild import manage_request
    await manage_request(ctx, *args, client=bot)


@bot.command()
async def guildfamily(ctx, *args):
    from commands.admincmds import paused
    if paused:
        return
    from commands.guild_family import manage_request
    await manage_request(ctx, *args, client=bot)


@bot.command()
async def userfamily(ctx, *args):
    from commands.admincmds import paused
    if paused:
        return
    from commands.user_family import manage_request
    await manage_request(ctx, *args, client=bot)


@bot.command()
async def close(ctx):
    from commands.admincmds import shutdown
    await shutdown(ctx, bot)


@bot.command()
async def shutdown(ctx):
    from commands.admincmds import shutdown
    await shutdown(ctx, bot)


@bot.command()
async def pause(ctx):
    from commands.admincmds import pause
    await pause(ctx, bot)


make_directories()

bot.run(os.getenv("TOKEN"))
