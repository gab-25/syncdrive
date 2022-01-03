from selenium import webdriver


class GDrive:
    idDrive: int

    def __init__(self, idDrive, args):
        self.idDrive = idDrive
        GDrive.__login()
        for arg in args:
            try:
                getattr(GDrive, arg)()
            except AttributeError:
                print("Param {0} not found, use --help for list params".format(arg))

    def __login():
        driver = webdriver.Firefox()
        driver.get("https://accounts.google.com/signin")
        pass

    def upload():
        """upload: upload file into google drive"""
        print("upload function")

    def download():
        """download: download file from google drive"""
        print("download function")
