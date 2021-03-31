async def shutdown(ctx, client):
    from embeds import create_custom_embed
    from discord import Colour
    if ctx.author.id != 784473264755834880:
        embed = create_custom_embed(
            embed_message="You are not permitted to close the bot!",
            user=ctx.author,
            colour=Colour.dark_red()
        )
        await ctx.send(embed=embed)
        return
    confirmation_message = await ctx.send(
        embed=create_custom_embed(
            embed_title="Confirmation",
            embed_message="You're about to shut me down. Do you really want to continue this process?",
            user=ctx.author,
            colour=Colour.blue()
        )
    )
    from utils import ReturnCodes, get_confirmation
    confirmation = await get_confirmation(confirmation_message, ctx.author, client)
    if confirmation == ReturnCodes.SUCCESS:
        await ctx.send(
            embed=create_custom_embed(
                embed_message="I try to switch off. Please note the console for possible errors..",
                user=ctx.author,
                colour=Colour.dark_green()
            )
        )
        await client.close()
    elif confirmation == ReturnCodes.CANCELLED:
        await confirmation_message.delete()

    elif confirmation == ReturnCodes.TIMEOUT_ERROR:
        await confirmation_message.delete()

    elif confirmation == ReturnCodes.OTHER_ERROR:
        from embeds import handle_error
        await ctx.send(handle_error(confirmation, ctx.author))


async def manage_request(ctx, *args):
    args = [arg.lower() for arg in args]
    if len(args) != 1:
        # TODO Syntax Error
        await ctx.send("SYNTAX ERROR!")
    if args[0] == "guildfam":
        from guild_family import get_family
        from utils import ReturnCodes

        get_family_process = get_family(ctx.guild.id)
        if get_family_process == ReturnCodes.NOT_FOUND:
            await ctx.send("This guild has no default url.")
        else:
            await ctx.send(f"The default url of this guild is:```{get_family_process}```")
    if args[0] == "userfam":
        pass
