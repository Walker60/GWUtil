import os
import smtplib
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import keyboard
import pyautogui
import pytesseract
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import imageUtil

# Credentials are loaded from CoinWatch/.env (gitignored) - see .env.example
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = os.environ["SMTP_USERNAME"]
SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL", SMTP_USERNAME)

subject = "Gems Down to Right Price!"
body = "Buy Gems Now!"
msg = MIMEMultipart()
msg["From"] = SMTP_USERNAME
msg["To"] = RECIPIENT_EMAIL
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))


imagePath = "Images/"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(1)
keyboard.send('o')

while True:
    imageUtil.clickOnImage(imagePath + "BuyGem", con=.8)

    gemCords = imageUtil.waitForImageCords(imagePath + "gems", con=.95)
    x = gemCords[0] + 180
    y = gemCords[1]
    sys.stdout.flush()
    im1 = pyautogui.screenshot(region=(int(x), int(y), 38, 40))
    im1.save("savedimage.png")

    price = pytesseract.image_to_string(im1)
    print(price)
    sys.stdout.flush()
    if int(price[1]) < 4:
        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, RECIPIENT_EMAIL, msg.as_string())
            server.quit()
            print("Email sent successfully.")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    imageUtil.clickOnImage(imagePath + "GemStore", con=.95)
    pyautogui.moveTo(10, 10)
    time.sleep(30)
