import smtplib
from email.message import EmailMessage

def send_email(receiver, subject, content):
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = receiver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('your_email@gmail.com', 'your_app_password')  # Use App Passwords
        smtp.send_message(msg)