import requests


def check_page(title):
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "revisions"
    }

    res = requests.get(url="https://en.wikipedia.org/w/api.php", params=params)
    data = res.json()

    try:
        error_page = data["query"]["pages"]["-1"]
        return False
    except KeyError:
        return True
