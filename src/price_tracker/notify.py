import os
from price_tracker import constants
# Tu treba napravit da nije samo CLI neg priko GUI
import bcrypt
from getpass import getpass
from twilio.rest import Client
import configparser


def email_handler():

    email = input("Enter your email: ")
    password = input("Enter your password: ")
    #password = getpass(prompt="Enter your password: ")
    #Login
    if os.path.exists(constants.SAVE_PATH):
        with open(constants.SAVE_PATH) as file:
            user, passw = file.readline().strip().split(":")
            if email == user:
                if bcrypt.checkpw(password.encode('utf-8'), passw.encode('utf-8')):
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
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            file.write(f"{email}:{hashed_password.decode('utf-8')}\n")
            print("Register successful")
            return True


def phone_handler(item):
    config = configparser.ConfigParser()
    config.read('../../cf.ini')

    message = f"There is a price drop of {item.percentage*100} % for {item.title}.\nIt is now {item.price} €"
    account_sid = config["phone"]["sid"]
    auth_token = config["phone"]["token"]
    client = Client(account_sid, auth_token)
    print(config["phone"]["from"])
    print(config["phone"]["to"])

    _ = client.messages.create(
        from_=config["phone"]["from"],
        body=message,
        to=config["phone"]["to"]
    )
