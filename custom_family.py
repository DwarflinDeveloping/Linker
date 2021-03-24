def manage_search(search):
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

    return search_url
