from cryptography.fernet import Fernet


class PasswordManager:

    def __init__(self):
        self.key = None
        self.passwords = None
        self.passwords_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, "wb")as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, "rb") as f:
            self.key = f.read()

    def create_password_file(self, path, initial_values=None):
        self.passwords_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    def loar_password_file(self, path):
        self.passwords_file = path

        with open(path, "r") as f:
            for line in f:
                site, encrypted = line.split(":")
                self.passwords_dict[site] = Fernet(self.key).decrypt(encrypted.encode())

    def add_password(self, site, password):
        self.passwords_dict[site] = password

        if self.passwords_file is not None:
            with open(self.passwords_file, "a") as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.passwords_dict[site]


def main():
    password = {
        "Emma": "Kzt#h2g8m@9Xf",
        "Liam": "WpL!c1r7o@8Nv",
        "Olivia": "FqR$b6t1p@9Zx",
        "Noah": "TgM%h3y8q@2Kl",
        "Ava": "ZxJ#t9r6p@1Wc",
        "Isabella": "HfV!y7o8m@3Nb",
        "Jackson": "CbK$r5p9t@6Xg",
        "Sophia": "NvM%h1y3q@7Wj",
        "Aiden": "XtZ#o6m8p@2Fq",
        "Mia": "LkR!c9t7q@1Hf",
        "Lucas": "YgJ$b5o6m@8Tp",
        "Charlotte": "WzV!h2p9t@7Nx",
        "Elijah": "KmT#y1r7o@6Cb",
        "Harper": "HjR$b3m8p@5Fq",
        "Mason": "GxL!h9t6q@4Zx",
        "Amelia": "CpM%o8r5p@3Kz",
        "Ethan": "NbK$y7m4t@2Wp",
        "Evelyn": "XgJ!c6p3o@1Tg",
        "Alexander": "ZtV$h5r2m@9Lk",
        "Abigail": "WfR!y4o1p@8Yg",
        "William": "TpM#c3m9t@7Km",
        "Scarlett": "HxL$b2p8o@6Hj",
        "Michael": "KzJ!h1r7m@5Gx",
        "Elizabeth": "YtV$o9p6t@4Cp",
        "Benjamin": "WpM%c8r5o@3Nb",
        "Avery": "GbK#y7m4p@2Xg",
        "Jacob": "NxJ!h6p3t@1Zt",
        "Ella": "CgR$o5r2o@9Wf",
        "James": "ZkL!c4m1p@8Tp",
        "Victoria": "HtM#h3p9t@7Hx"
    }

    pm = PasswordManager()

    print("""What do you want to do?
    (1) Create a new key
    (2) Load an existing key
    (3) Create new password file
    (4) Load exising password file
    (5) Add a new password
    (q) Quit
    """)

    done = False

    while not done:

        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input("Enter a path: ")
            pm.load_key(path)
        elif choice == "3":
            path = input("Enter a path: ")
            pm.create_password_file(path, password)
        elif choice == "4":
            path = input("Enter a path: ")
            pm.loar_password_file(path)
        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        elif choice == "6":
            site = input("What site do you want: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif choice == "q":
            done = True
            print("Bye")
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()





