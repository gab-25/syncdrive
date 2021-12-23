import sys
from enum import Enum
from gdrive.gdrive import GDrive
from gdrive.helpers import help

print("GSYNCPY - GOOGLE SYNC TOOL")
print("")


class Command(Enum):
    help = "--help"
    upload = "--upload"
    download = "--download"


def main():
    args = sys.argv
    del args[0]
    args = " ".join([str(elem) for elem in args])

    gdrive = GDrive(0)

    if Command.help.value in args:
        help(Command)
    elif Command.upload.value in args:
        gdrive.upload()
    elif Command.download.value in args:
        gdrive.download()
    else:
        print("Error: invalid arguments, use --help for documentation")


if __name__ == "__main__":
    main()
