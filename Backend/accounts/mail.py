from config import SMTP_HOST, SMTP_PASSWORD, SMTP_USER
from utils import exists


import yagmail
import random


def get_random_code() -> str:
    while(True):
        code = str(random.randint(100000,999999))
        if not exists(code):
            return code

# Send an email to the specified receiver with the specified type and data
# Return True if the email is sent successfully, otherwise return False
def send_email(receiver: str, type: str, data: dict) -> bool:
    try:
        if type == "auth-code":
            yag = yagmail.SMTP(user=SMTP_USER,password=SMTP_PASSWORD,host=SMTP_HOST)
            code = data['code']
            contents = [
                f'[CyberSpace] Your code for registration is: {code}',
                "The code will be expired in 5 minutes. Please do not share it with anyone.",
                "Please ignore this email if you did not request for registration.",
                "--------------------------------------------------------------------------",
                "Sincerely, CyberSpace Team"
            ]
            yag.send(to=receiver,subject="Your code for registration",contents=contents)
            return True
    except:
        return False