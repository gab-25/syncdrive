import sys
from gdrive import GDrive
from helpers import Helpers


def run():
    print("SYNCPY - STORAGE SYNC TOOL")
    print()

    args = sys.argv
    del args[0]
    args = " ".join([str(elem) for elem in args])

    if args == "":
        raise Exception("invalid arguments, use --help for documentation")

    if "--help" in args:
        Helpers.help(args)
    else:
        GDrive(0, args.split())


if __name__ == "__main__":
    try:
        run()
    except Exception as ex:
        print("Error: {0}".format(ex))
