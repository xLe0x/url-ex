tlds = (".com", ".net", ".org", ".co", ".us", ".tk", ".xyz")


def links_formatter(links):
    valid_links = []
    for link in links:
        if link.endswith(tlds):
            valid_links.append(link)
            print(link)

    if len(valid_links) == 0:
        print("no url extracted")
