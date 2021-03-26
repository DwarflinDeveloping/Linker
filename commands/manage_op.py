trusted_members = [784473264755834880]
administrators = [784473264755834880]


async def manage_request(ctx, *args):
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
