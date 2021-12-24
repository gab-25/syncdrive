import sys
from gdrive.gdrive import GDrive
from gdrive.helpers import Helpers


def main():
    print("GSYNCPY - GOOGLE SYNC TOOL")
    print()

    args = sys.argv
    del args[0]
    args = " ".join([str(elem) for elem in args])

    if args == "":
        raise Exception("invalid arguments, use --help for documentation")

    if "--help" in args:
        Helpers.help(args)
    else:
        GDrive(0, args)


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print("Error: {msg}".format(msg=ex))
