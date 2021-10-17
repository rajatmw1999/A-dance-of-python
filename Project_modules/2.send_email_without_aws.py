from email_text import email_text
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "eganinjahattori@gmail.com"
password = "Eganinja@2021"
html = email_text
def email(rec):
    for x in range(5):
    
        receiver_email = rec
        message = MIMEMultipart("alternative")
        message["Subject"] = "Here's to first classes " + str(x)
        message["From"] = sender_email
        message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        # part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        # message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        print(rec,x,"sent!")

for x in ("ajithppnair@gmail.com","rajat.campk12@gmail.com","smridhi.baunthiyal7@gmail.com","smridhi.baunthiyal07@gmail.com","vivekcheema026@gmail.com","Sarthaksrishtiss18@gmail.com","sakshi1499@gmail.com", "pratyushsingh736@gmail.com"):
    email(x)