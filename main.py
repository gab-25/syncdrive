#!/bin/python3

import sys
from gdrivesync.gdrive import GDrive
from gdrivesync.helpers import Helpers


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
        GDrive(0, args.split())


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print("Error: {0}".format(ex))
