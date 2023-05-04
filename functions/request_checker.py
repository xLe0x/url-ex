import re
from functions.links_formatter import links_formatter


def request_checker(req):
    if req.ok:
        links = re.findall(
            "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            req.text,
        )
        links_formatter(links)
