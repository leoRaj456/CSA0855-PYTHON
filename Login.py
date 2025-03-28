def login():
            user = input("Username: ")
            passw = input("Password: ")
            with open("users.txt", "r") as f:
                for line in f.readlines():
                    us, pw = line.strip().split("|")
                    if user == us and passw == pw:
                        print("Login successful!")
                        return True
                print("Wrong username/password")
                return False
        
def menu():
            while True:
                log = login()
                if log:
                    print("Welcome to the menu!")
                    break
