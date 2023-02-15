import os
from price_tracker import constants
# Tu treba napravit da nije samo CLI neg priko GUI
import bcrypt
from getpass import getpass


def email_handler(hash_key):

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    #Login
    if os.path.exists(constants.SAVE_PATH):
        with open(constants.SAVE_PATH) as file:
            user, passw = file.readline().strip().split(":")
            if email == user:
                if bcrypt.checkpw((password+hash_key).encode('utf-8'), passw.encode('utf-8')):
                    print("Login successful")
                    return True
                else:
                    print("Login unsuccessful")
                    return False
            else:
                print("Login unsuccessful")
                return False

    #Register
    else:
        with open(constants.SAVE_PATH, 'w') as file:
            hashed_password = bcrypt.hashpw((password+hash_key).encode('utf-8'), bcrypt.gensalt())
            file.write(f"{email}:{hashed_password.decode('utf-8')}\n")
            print("Register successful")
            return True


hash_key = "123"
if __name__ == "__main__":
    email_handler(hash_key)