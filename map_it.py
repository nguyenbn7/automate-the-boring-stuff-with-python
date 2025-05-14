import logging, webbrowser
from urllib.parse import quote_plus, urljoin

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")


def open_google_map_in_webbrowser(address: str):
    if not address:
        raise Exception("Address is None or empty")

    url = urljoin("https://www.google.com/maps/place/", quote_plus(address))
    logging.debug(url)
    webbrowser.open(url)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("address", help="Address")

    args = parser.parse_args()

    address = args.address

    open_google_map_in_webbrowser(address)
