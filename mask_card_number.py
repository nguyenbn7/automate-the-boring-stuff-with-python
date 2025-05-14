import re

credit_card_pattern = re.compile(
    r"""
    ((\d{4})[-\s*]?\d{4}[-\s*]?\d{4}[-\s*]?(\d{4}))
    """,
    re.VERBOSE,
)


def mask_card(card: str, replace: str = "*", show_first_4=False):
    if not replace:
        raise Exception("replace character is None or empty")

    if show_first_4:
        return credit_card_pattern.sub(rf"\2{replace * 8}\3", card)

    return credit_card_pattern.sub(rf"{replace * 12}\3", card)


if __name__ == "__main__":
    from argparse import ArgumentParser, BooleanOptionalAction

    parser = ArgumentParser()

    parser.add_argument(
        "card", help="Credit card or debit card number, ex: 1234-5678-9101-1121"
    )

    parser.add_argument(
        "--first-4",
        help="Show first 4 digits (included last 4 digits). Default not show first 4 digits",
        action=BooleanOptionalAction,
        default=False,
    )

    parser.add_argument("--replace", help="Masking char. Default '*'", default="*")

    args = parser.parse_args()

    card = args.card
    show_first_4 = args.first_4
    replace = args.replace

    print(mask_card(card, replace=replace, show_first_4=show_first_4))
