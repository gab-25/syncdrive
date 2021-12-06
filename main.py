import sys
from gdrive import GDrive


class Main:

    def func(self, args):
        print("GSYNCPY - GOOGLE SYNC TOOL")
        print("")

        if "--help" in args:
            help()
        elif "--upload" in args:
            GDrive.upload()
        elif "--download" in args:
            GDrive.download()
        else:
            print("Error: invalid arguments, use --help for documentation")

    def help():
        print("help")


if __name__ == "__main__":
    args = sys.argv
    del args[0]

    str_args = " ".join([str(elem) for elem in args])

    Main.func(str_args)
