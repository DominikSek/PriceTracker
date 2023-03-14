import os
from price_tracker import constants
# Tu treba napravit da nije samo CLI neg priko GUI
import bcrypt
from getpass import getpass
from twilio.rest import Client
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

import smtplib

mail_template = """
<html>
  <head>
    <style>
      {style}
    </style>
  </head>
  <body>
    <h1> Price alert!!! </h1>
    <p>The price of the item {product_name} has dropped from {old_price} € to {new_price} €.</p>
    <p>Here is a picture of the item:</p>
    <div class='outer'>
      <div class='inner'>
        <img src="{image_url}" alt="{product_name}" style="max-width: 100%;">
      </div>
    </div>
    <p><a href="{product_url}">Click here to view the product on Amazon.</a></p>
    <p>Don't miss out on this great deal!</p>
    <p>Best regards,</p>
    <p>Dominik</p>
  </body>
</html>
"""


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

    _ = client.messages.create(
        from_=config["phone"]["from"],
        body=message,
        to=config["phone"]["to"]
    )


def outlook_handler(item, mail_to):
    config = configparser.RawConfigParser()
    config.read('../../cf.ini')

    mail = mail_template.format(
        product_name = item.title,
        old_price = item.alert_price,
        new_price = item.price,
        image_url = item.image,
        product_url = item.url,
        style = """ 
            p {
            font-size: 16px;
            line-height: 24px;
            margin-bottom: 16px;
          }
          img {
            max-width: 100%;
            height: auto;
            vertical-align: middle;
          }
          a {
            color: #0078d7;
            text-decoration: none;
          }
          a:hover {
            text-decoration: underline;
          }
          inner {
            max-width: 30%; 
            margin: auto;
          }
           outer {
           border: 1px solid #ddd; 
           border-radius: 4px; 
           padding: 10px; 
           text-align: center;
          }
        """
    )

    msg = MIMEMultipart()
    msg['From'] = "Price Checker"
    msg['To'] = "***"
    msg['Subject'] = f"Price drop {item}"
    msg.attach(MIMEText(mail, "html"))

    s = smtplib.SMTP("smtp.office365.com", 587,  timeout=120)

    s.ehlo()
    s.starttls()
    s.ehlo()

    s.login(config["email"]["server_address"], config["email"]["server_pass"])
    s.sendmail(config["email"]["server_address"], mail_to, msg.as_string())

    s.quit()
