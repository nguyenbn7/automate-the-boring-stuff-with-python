#! python3
"""
rename_dates.py - Renames filenames with American MM-DD-YYYY date format
to European DD-MM-YYYY.

* Note: I use pathlib rather than os due to simplicity to use and argparse for
handle argument.
"""


import pathlib
import re
import shutil


def rename_files_from_amer_to_eu_style_date(folder: str):
    date_pattern = re.compile(
        r"""
      ^(.*?)              # all text before date
      ((0|1)?\d)-         # one or two digits for month
      ((0|1|2|3)?\d)-     # one or two digits for the day
      ((19|20)\d\d)       # four digits for year
      (.*?)$              # all text after the date
      """,
        re.VERBOSE,
    )

    folder_path = pathlib.Path(folder).resolve()

    for amer_filename in folder_path.glob("*"):
        mo = date_pattern.search(amer_filename.name)

        if mo is None:
            continue

        before_part = mo.group(1)
        month_part = mo.group(2)
        day_part = mo.group(4)
        year_part = mo.group(6)
        after_part = mo.group(8)

        euro_filename = (
            before_part + day_part + "-" + month_part + "-" + year_part + after_part
        )

        abs_working_dir = folder_path.absolute()
        abs_amer_filename = abs_working_dir / amer_filename
        abs_euro_filename = abs_working_dir / euro_filename

        print(f'Renaming "{abs_amer_filename}" to "{abs_euro_filename}"...')
        shutil.move(abs_amer_filename, abs_euro_filename)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument(
        "directory",
        help="Directory contains files that have American-style dates (MM-DD-YYYY) in their names and needs them renamed to Europeanstyle dates (DD-MM-YYYY)",
        type=str,
    )

    args = parser.parse_args()

    rename_files_from_amer_to_eu_style_date(args.directory)
