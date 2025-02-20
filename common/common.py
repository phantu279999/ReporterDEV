import json
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup


def count_word(text):
	if not text:
		return 0
	soup = BeautifulSoup(text, 'html.parser')
	texts = [len(it.strip().split(" ")) for it in soup.strings if it.strip()]
	return sum(texts)


def get_reading_time(word_count, words_per_minute=200):
	""" Read avg time of a news"""
	if word_count <= 0:
		return 0
	return round(word_count / words_per_minute)


def send_email(body, to_email, subject="Reporter: You have a new noti"):
	with open('config_email.json', 'r') as f:
		email = json.load(f)

	smtp_server = "smtp.gmail.com"
	port = 465
	sender_email = email['sender_email']
	password = email['password']

	# Create a MIMEText object with the email body
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = to_email
	message["Subject"] = subject

	# Attach the body to the email
	message.attach(MIMEText(body, "plain"))

	# Establish a secure connection with the SMTP server
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		# Log in to your Gmail account
		server.login(sender_email, password)

		# Send the email
		server.sendmail(sender_email, to_email, message.as_string())


if __name__ == '__main__':
	send_email("Hello World!", "phantu279999@gmail.com")
