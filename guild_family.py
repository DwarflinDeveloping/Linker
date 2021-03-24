def set_family(guild_id, family_url):
    from utils import ReturnCodes

    try:
        guild_family_file = open(f"data/guild_familys/{str(guild_id)}.txt", "w")
        guild_family_file.write(family_url)
        guild_family_file.close()

        return ReturnCodes.SUCCESS
    except:
        return ReturnCodes.OTHER_ERROR


def clear_family(guild_id):
    from utils import ReturnCodes

    import os
    if os.path.isfile(f"data/guild_familys/{str(guild_id)}.txt"):
        os.remove(f"data/guild_familys/{str(guild_id)}.txt")
        return ReturnCodes.SUCCESS
    else:
        return ReturnCodes.NOT_FOUND


def get_family(guild_id):
    from utils import ReturnCodes
    import os

    if os.path.isfile(f"data/guild_familys/{str(guild_id)}.txt"):
        guild_family_file = open(f"data/guild_familys/{str(guild_id)}.txt", "r")
        guild_family = guild_family_file.read()
        guild_family_file.close()
        return guild_family
    else:
        return ReturnCodes.NOT_FOUND
