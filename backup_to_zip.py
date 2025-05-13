#! python3
"""
back_to_zip.py - Copies an entire folder and its content into
a ZIP file whose file name increments

*Note: I use pathlib rather than os due to simplicity to use and argparse for
handle argument.
"""


from pathlib import Path
from zipfile import ZipFile


def to_zip(folder: str):
    folder_path = Path(folder).resolve()

    if not folder_path.is_dir():
        raise Exception(f"'{folder}' is not a directory")

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zip_filename = folder_path.name + "_" + str(number) + ".zip"
        if not (folder_path / zip_filename).exists():
            break
        number += 1

    print(f"Creating {zip_filename}...")

    print(folder_path)

    with ZipFile(folder_path.parent / zip_filename, "w") as backup_zip:
        for root, dirs, filenames in folder_path.walk():
            folder_to_archive = root.relative_to(folder_path.parent)

            print(f"Adding files in {folder_to_archive}...")

            # Add the current folder to the ZIP file.
            backup_zip.write(folder_to_archive)

            # Add all the files in this folder to the ZIP file.
            for filename in filenames:
                new_base = folder_path.name + "_"

                if filename.startswith(new_base) and filename.endswith(".zip"):
                    continue  # don't backup the backup ZIP files

                backup_zip.write(folder_to_archive / filename)

    print("Done.")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument(
        "directory", help="Folder or Directory you want to archive", type=str
    )

    args = parser.parse_args()

    to_zip(args.directory)
