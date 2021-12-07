import sys
from gdrive.gdrive import GDrive


print("GSYNCPY - GOOGLE SYNC TOOL")
print("")


def main():
    args = sys.argv
    del args[0]
    args = " ".join([str(elem) for elem in args])

    if "--help" in args:
        help()
    elif "--upload" in args:
        GDrive.upload()
    elif "--download" in args:
        GDrive.download()
    else:
        print("Error: invalid arguments, use --help for documentation")


if __name__ == "__main__":
    main()
