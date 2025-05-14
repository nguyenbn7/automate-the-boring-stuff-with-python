#! python3
"""lucky.py - Opens several Google search results.

* Note: this one is broken due to google search capcha or something prevent to get body
"""
from logging import DEBUG, INFO, basicConfig, debug
import webbrowser
from urllib.parse import quote_plus

from bs4 import BeautifulSoup
import requests


basicConfig(level=INFO)


def open_webbrowser_with_several_results(search_term: str, open_links: int = 5):
    print("Googling...")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    res = requests.get(
        "http://google.com/search",
        params={
            "client": "google-csbe",
            "q": quote_plus(search_term),
            "cx": "00255077836266642015:u-scht7a-8i",
            "hl": "en",
        },
        headers=headers,
    )

    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    link_elems = soup.select(".r a")
    debug(f"\n{link_elems}\n")

    for i in range(min(open_links, len(link_elems))):
        debug(f'{link_elems[i].get("href")}\n')
        webbrowser.open(link_elems[i].get("href"))


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("search", help="Search term")
    parser.add_argument(
        "--open-links",
        help="Number of links after searching will be opened. Default 5",
        default=5,
        type=int,
    )

    args = parser.parse_args()

    search_term = args.search
    open_links = args.open_links

    open_webbrowser_with_several_results(search_term=search_term, open_links=open_links)
