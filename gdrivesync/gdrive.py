from gdrivesync.login import Login


class GDrive:
    idDrive: int

    def __init__(self, idDrive: int, args: list):
        self.idDrive = idDrive
        Login()
        for arg in args:
            try:
                getattr(GDrive, arg)()
            except AttributeError:
                print("Param {0} not found, use --help for list params".format(arg))

    def upload():
        """upload: upload file into google drive"""
        print("upload function")

    def download():
        """download: download file from google drive"""
        print("download function")
