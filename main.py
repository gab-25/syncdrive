import sys
from gdrive.gdrive import GDrive


print("GSYNCPY - GOOGLE SYNC TOOL")
print("")


def main():
    args = sys.argv
    del args[0]
    args = " ".join([str(elem) for elem in args])

    gdrive = GDrive(0)

    if "--help" in args:
        help()
    elif "--upload" in args:
        gdrive.upload()
    elif "--download" in args:
        gdrive.download()
    else:
        print("Error: invalid arguments, use --help for documentation")


if __name__ == "__main__":
    main()
