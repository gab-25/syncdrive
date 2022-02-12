import sys
from drive import Drive
from helpers import Helpers


def run() -> bool:
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
        Drive(0, args.split())

    return True


if __name__ == "__main__":
    try:
        run()
    except Exception as ex:
        print("Error: {0}".format(ex))
