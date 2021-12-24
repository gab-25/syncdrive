class GDrive:
    idDrive: int

    def __init__(self, idDrive, args):
        self.idDrive = idDrive
        for i, arg in enumerate(args):
            if ("--" in arg):
                getattr(GDrive, arg.replace("--", ""))

    def upload():
        """upload file into google drive"""
        print("upload")

    def download():
        """download file from google drive"""
        print("download")
