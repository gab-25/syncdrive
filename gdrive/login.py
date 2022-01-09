import getpass


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
            user.email = input("Email: ")
            user.password = getpass.getpass("Password: ")

        self.user = user

        Login.__check_credts(self)
        Login.__singin(self)

    def __singin(self):
        form_data = {
            "Email": self.user.email,
            "Password": self.user.password
        }

    def __check_credts(self):
        pass
