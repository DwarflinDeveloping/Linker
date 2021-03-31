def handle_error(error, user):
    from utils import ReturnCodes
    from discord import Embed, Colour

    if error == ReturnCodes.OTHER_ERROR:
        error_embed = Embed(
            title=
            "Error",
            description=
            "An unknown error has occurred.\n"
            "If that happens every time, please contact our support.",
            colour=
            Colour.dark_red()
        )
        error_embed.set_footer(text=f"Request of {user}", icon_url=user.avatar_url)
        return error_embed


def create_custom_embed(embed_message, user, embed_title="Error", colour=None):
    icon = user.avatar_url
    if colour is None:
        from discord import Colour
        colour = Colour.dark_red()
    from discord import Embed
    error_embed = Embed(title=embed_title, description=embed_message, colour=colour)
    error_embed.set_footer(text=f"Request of {user}", icon_url=icon)
    return error_embed
