#! python3
"""phone_and_email.py - Finds phone numbers and email addresses on the clipboard."""

import re

import pyperclip

phone_pattern = re.compile(
    r"""(
        (\d{3}|\(\d{3}\))?                  # area code
        (\s|-|\.)?                          # seperator
        (\d{3})                             # first 3 digits
        (\s|-|\.)                           # seperator
        (\d{4})                             # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
    )""",
    re.VERBOSE,
)


def extract_phone_numbers(text: str):
    matches = []

    for groups in phone_pattern.findall(text):
        phoneNum = "-".join([groups[1], groups[3], groups[5]])
        if groups[8] != "":
            phoneNum += " x" + groups[8]
        matches.append(phoneNum)

    return matches


email_pattern = re.compile(
    r"""(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
    )""",
    re.VERBOSE,
)


def extract_emails(text: str):
    return [groups[0] for groups in email_pattern.findall(text)]


if __name__ == "__main__":
    text = pyperclip.paste()
    
    matches = extract_phone_numbers(text)
    matches.extend(extract_emails(text))

    if len(matches) > 0:
        pyperclip.copy("\n".join(matches))
        print("Copied to clipboard:")
        print("\n".join(matches))
    else:
        print("No phone numbers or email addresses found.")
