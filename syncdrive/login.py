from selenium import webdriver
import time


class User:
    email: str
    password: str

    def __init__(self, email: str = None, password: str = None):
        self.email = email
        self.password = password


class Login:
    user: User

    def __init__(self, user: User = None):
        if user is None:
            print("GOOGLE LOGIN")
            user = User()
            Login.__singin(self)

    def __singin(self):
        driver = webdriver.Chrome()
        driver.get("https://accounts.google.com");
        time.sleep(5)
        driver.close()
