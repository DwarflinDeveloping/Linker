async def manage_request(ctx, *args):
    if len(args) == 0:
        # TODO Syntax
        pass

    if args[0] == "get":
        get_process = get_custom_words(ctx.author.id)
        from utils import ReturnCodes
        if get_process == ReturnCodes.NOT_FOUND:
            await ctx.send("You have no custom words.")
        else:
            await ctx.send(f"Your custom words are:```{get_process}```")

    elif args[0] == "clear":
        clear_process = clear_custom_words(ctx.author.id)
        from utils import ReturnCodes
        if clear_process == ReturnCodes.NOT_FOUND:
            await ctx.send("You have no custom words.")
        elif clear_process == ReturnCodes.OTHER_ERROR:
            await ctx.send("An unknown error has occurred.\n"
                           "If that happens every time, contact our support.")
        elif clear_process == ReturnCodes.SUCCESS:
            await ctx.send("Your custom words successfully cleared.")

    elif args[0] == "remove":
        add_process = remove_custom_word(ctx.author.id, args[1])
        from utils import ReturnCodes
        if add_process == ReturnCodes.SUCCESS:
            await ctx.send(f"The word `{args[1]}` was successfully removed.")
        elif add_process == ReturnCodes.NOT_FOUND:
            await ctx.send("You don't have this custom word.")

    elif args[0] == "add":
        add_process = create_custom_word(ctx.author.id, args[1], args[2])
        from utils import ReturnCodes
        if add_process == ReturnCodes.SUCCESS:
            await ctx.send(f"The word `{args[1]}` was successfully set to the url `{args[2]}`")


def create_custom_word(user_id, custom_word, url):
    import json
    import os
    from utils import ReturnCodes

    if os.path.isfile(f"data/custom_words/users/{user_id}.json"):
        with open(f"data/custom_words/users/{user_id}.json", "r") as json_file:
            custom_words = json.load(json_file)
        custom_words[custom_word] = url
        json_file.close()
    else:
        custom_words = {custom_word: url}
    with open(f"data/custom_words/users/{user_id}.json", "w") as json_file:
        json_file.write(json.dumps(custom_words, indent=4))
    json_file.close()

    return ReturnCodes.SUCCESS


def remove_custom_word(user_id, custom_word):
    import json
    import os
    from utils import ReturnCodes

    if not os.path.isfile(f"data/custom_words/users/{user_id}.json"):
        return ReturnCodes.NOT_FOUND

    with open(f"data/custom_words/users/{user_id}.json", "r") as json_file:
        custom_words = json.load(json_file)
    if custom_word not in custom_words:
        return ReturnCodes.NOT_FOUND
    del custom_words[custom_word]
    json_file.close()

    with open(f"data/custom_words/users/{user_id}.json", "w") as json_file:
        json_file.write(json.dumps(custom_words, indent=4))
    json_file.close()

    return ReturnCodes.SUCCESS


def get_custom_words(user_id):
    import os
    import json
    from utils import ReturnCodes

    if os.path.isfile(f"data/custom_words/users/{user_id}.json"):
        with open(f"data/custom_words/users/{user_id}.json", "r") as json_file:
            custom_words = json.load(json_file)
        json_file.close()
        return json.dumps(custom_words, indent=4)
    else:
        return ReturnCodes.NOT_FOUND


def clear_custom_words(user_id):
    import os
    from utils import ReturnCodes

    file_path = f"data/custom_words/users/{user_id}.json"

    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
            return ReturnCodes.SUCCESS
        except:
            return ReturnCodes.OTHER_ERROR
    else:
        return ReturnCodes.NOT_FOUND
