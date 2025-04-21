import pywhatkit
from dotenv import load_dotenv
import os

def send_whatsapp_message(receiver, message, wait_time):
  pywhatkit.sendwhatmsg_instantly(receiver, message, wait_time)

load_dotenv()

RECEIVER_NUMBER = os.getenv("RECEIVER_NUMBER")

MESSAGE = "HELO"
WAIT_TIME = 32 #Lower numbers will only have the text in the text field and not sent
send_whatsapp_message(RECEIVER_NUMBER, MESSAGE, WAIT_TIME)