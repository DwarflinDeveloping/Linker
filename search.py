def manage_search(message):
    import re
    links = ""
    items = re.findall("\\{[^\\}]*\\}", message.content)
    searches = []
    for item in items:
        item = re.sub('[\\{\\}]', '', item)
        item = re.sub('\\s', '_', item)
        searches += [item]

    for search in searches:
        if ":" in search:
            from custom_family import manage_search
            search_url = manage_search(search)
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

            if os.path.isfile(f"data/custom_words/guilds/{str(message.guild.id)}.json"):
                guild_custom_word_file = open(f"data/custom_words/guilds/{str(message.guild.id)}.json", "r")
                import json
                guild_custom_words = json.loads(guild_custom_word_file.read())
                if search in guild_custom_words:
                    search_url = guild_custom_words[search]
                guild_custom_word_file.close()

            if os.path.isfile(f"data/custom_words/users/{str(message.author.id)}.json"):
                user_custom_word_file = open(f"data/custom_words/users/{str(message.author.id)}.json", "r")
                import json
                guild_custom_words = json.loads(user_custom_word_file.read())
                if search in guild_custom_words:
                    search_url = guild_custom_words[search]
                user_custom_word_file.close()
        if search.startswith("$"):
            search_url = search_url.replace("$", "")
            search_text = search_url
        else:
            search_text = f"<{search_url}>"
        links += search_text + "\n"
    return links
