import requests
from api.CheckPage import check_page


def fetch_page(title):
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "links",
        "pllimit": "max",
        "redirects": ""
    }

    res = requests.get(url="https://en.wikipedia.org/w/api.php", params=params)
    data = res.json()

    pages = data["query"]["pages"]
    page_titles = []

    for key, val in pages.items():
        for link in val["links"]:
            if link["ns"] == 0:
                title = link["title"]
                if check_page(title):
                    page_titles.append(title)
                    print(title)

    return page_titles
