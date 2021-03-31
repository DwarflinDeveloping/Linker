from enum import Enum


class FamilyTemplates:
    YOUTUBE = "https://www.youtube.com/%ARTICLE%"
    TWITCH = "https://twitch.tv/%ARTICLE%"

    MINECRAFT = "https://minecraft.fandom.com/%WIKI%/wiki/%ARTICLE%"
    FANDOM = "https://%WIKI%.fandom.com/wiki/%ARTICLE%"
    GAMEPEDIA = "https://%WIKI%.gamepedia.com/%ARTICLE%"
    WIKIPEDIA = "https://%WIKI%.wikipedia.org/wiki/%ARTICLE%"


class ReturnCodes(Enum):
    SUCCESS = 0
    CANCELLED = 1
    TIMEOUT_ERROR = 2
    OTHER_ERROR = 3
    SYNTAX_ERROR = 4
    PERMISSION_ERROR = 5
    NOT_FOUND = 6
    PARAMTER_ERROR = 7
    VARIABLE_INVAILED = 8
    NO_CHANGES = 9


class Cancelled(Exception):
    pass


def get_family_template(search):
    search = search.lower()
    if search.startswith("wikipedia-"):
        return FamilyTemplates.WIKIPEDIA.replace("%WIKI%", search.replace("wikipedia-", ""))

    elif search.startswith("minecraft-"):
        return FamilyTemplates.MINECRAFT.replace("%WIKI%", search.replace("minecraft-", ""))

    elif search.startswith("fandom-"):
        return FamilyTemplates.MINECRAFT.replace("%WIKI%", search.replace("fandom-", ""))

    elif search.startswith("gamepedia-"):
        return FamilyTemplates.MINECRAFT.replace("%WIKI%", search.replace("gamepedia-", ""))

    elif search == "youtube":
        return FamilyTemplates.YOUTUBE

    elif search == "twitch":
        return FamilyTemplates.TWITCH

    else:
        return ReturnCodes.NOT_FOUND


async def get_confirmation(confirmation_message, confirmation_user, client):
    await confirmation_message.add_reaction("✅")
    await confirmation_message.add_reaction("❌")

    def check(reaction, user):
        if user != confirmation_user:
            return False
        if str(reaction.emoji) == "✅":
            return True
        if str(reaction.emoji) == "❌":
            raise Cancelled("CANCELL")

    import asyncio
    try:
        await client.wait_for("reaction_add", timeout=10.0, check=check)
        return ReturnCodes.SUCCESS
    except Cancelled:
        return ReturnCodes.CANCELLED
    except asyncio.TimeoutError:
        return ReturnCodes.TIMEOUT_ERROR
    except:
        return ReturnCodes.OTHER_ERROR
