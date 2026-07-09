import smtplib
from email.message import EmailMessage
from config import SENDER_EMAIL , SMTP_SERVER , PORT , PASSWORD
from pathlib import Path
import mimetypes

def send_email(recipient_email , subject , body , attachment_path):

    email_object = EmailMessage()

    email_object["From"] = SENDER_EMAIL
    email_object["To"] = recipient_email
    email_object["Subject"] = subject

    email_object.set_content(body)

    with open(attachment_path , "rb") as file:
        file_data = file.read()

    path = Path(attachment_path)

    file_name = path.name

    mimetype , encoding = mimetypes.guess_file_type(attachment_path)

    if mimetype is None:
        mimetype = "application/octet-stream"

    maintype , subtype = mimetype.split("/")

    email_object.add_attachment(
        file_data, 
        maintype=maintype, 
        subtype=subtype, 
        filename=file_name
        )

    server = smtplib.SMTP(SMTP_SERVER , PORT)

    server.starttls()

    server.login(SENDER_EMAIL , PASSWORD)

    server.sendmail(SENDER_EMAIL , recipient_email , email_object.as_bytes())

    server.quit()



