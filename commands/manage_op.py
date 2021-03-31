trusted_members = [784473264755834880]
administrators = [784473264755834880]


async def manage_request(ctx, *args):
    args = [arg.lower() for arg in args]
    if ctx.author.id not in administrators:
        from embeds import create_custom_embed
        from discord import Colour
        await ctx.send(
            embed=create_custom_embed(
                embed_message=f"You are not allowed to change operators rights.",
                user=ctx.author,
                colour=Colour.dark_red()
            )
        )
        return
    global trusted_members
    if args[0] == "get" or args[0] == "query":
        from embeds import create_custom_embed
        from discord import Colour
        operators = ""
        for operator in trusted_members:
            operators += f"{operator}\n"
        await ctx.send(
            embed=create_custom_embed(
                embed_title="Operator list",
                embed_message=f"```{operators}```",
                user=ctx.author,
                colour=Colour.blue()
            )
        )
        return
    if args[0] == "rem" or args[0] == "remove":
        if len(args) != 2:
            # TODO Syntax Error
            await ctx.send("Wrong use! Please use this:"
                           f"```%op {args[0]} <user id>```")
            return
        if args[1] not in trusted_members:
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_message=f"The user `{args[1]}` has no operator rights",
                    user=ctx.author,
                    colour=Colour.dark_red()
                )
            )
            return
        trusted_members.remove(args[1])
        from embeds import create_custom_embed
        from discord import Colour
        await ctx.send(
            embed=create_custom_embed(
                embed_message=f"The operator rights of this user have been removed:```{args[1]}```",
                user=ctx.author,
                colour=Colour.dark_green()
            )
        )
        return
    if args[0] == "add":
        if len(args) != 2:
            await ctx.send("Wrong use! Please use this:"
                           f"```%op {args[0]} <user id>```")
            return
        if args[1] in trusted_members:
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_message=f"The user `{args[1]}` already has operator rights.",
                    user=ctx.author,
                    colour=Colour.dark_red()
                )
            )
            return
        trusted_members += [args[1]]
        from embeds import create_custom_embed
        from discord import Colour
        await ctx.send(
            embed=create_custom_embed(
                embed_title="Sucess",
                embed_message=f"The operator rights have been added to this user:```{args[1]}```",
                user=ctx.author,
                colour=Colour.dark_green()
            )
        )
        return
