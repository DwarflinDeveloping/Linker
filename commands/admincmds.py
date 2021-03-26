async def manage_request(ctx, *args):
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
