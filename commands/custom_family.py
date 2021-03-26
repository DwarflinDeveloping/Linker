def manage_search(search):
    from utils import get_family_template, ReturnCodes
    search_family = search.split(":")[0].replace("$", "")
    get_progess = get_family_template(search_family)
    search_request = search.split(":")[1]
    if get_progess != ReturnCodes.NOT_FOUND:
        search_url = get_progess.replace("%ARTICLE%", search_request)
    else:
        search_url = f"https://{search_family}/{search_request}"

    return search_url
