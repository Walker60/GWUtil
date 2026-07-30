from pyautogui import *
import pyautogui
import time
import keyboard
import sys
sys.path.insert(1, 'C:/Users/12069/Dropbox/Scripts/Bots/Util')
sys.path.insert(1, 'C:/Users/Chris Walker/Dropbox/Scripts/Bots/Util')
import imageUtil
import pytesseract
from PIL import Image
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "fallenwon@gmail.com"
SMTP_PASSWORD = "gmsb tkgx rqnc rcos"
RECIPIENT_EMAIL = "fallenwon@gmail.com"

# Create the email message
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

while(1):
	imageUtil.clickOnImage(imagePath + "BuyGem", con = .8)

	while (gemCords := imageUtil.findImageCords(imagePath + "gems", con = .95)) == None:
		time.sleep(1)
	x = gemCords[0] + 180
	y = gemCords[1] 
	sys.stdout.flush()
	im1 = pyautogui.screenshot(region=(int(x),int(y),38, 40))
	im1.save("savedimage.png")

	price = pytesseract.image_to_string(im1)
	print(price)
	sys.stdout.flush()
	if int(price[1]) < 4:
		try:
			# Connect to the SMTP server
			server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
			server.starttls()

			# Log in to your Gmail account
			server.login(SMTP_USERNAME, SMTP_PASSWORD)

			# Send the email
			server.sendmail(SMTP_USERNAME, RECIPIENT_EMAIL, msg.as_string())

			# Close the connection
			server.quit()                                                                     
			print("Email sent successfully.")
			break
		except Exception as e:
			print(f"An error occurred: {str(e)}")

	imageUtil.clickOnImage(imagePath + "GemStore", con = .95)
	pyautogui.moveTo(10,10)
	time.sleep(30)

