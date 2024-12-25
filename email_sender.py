import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Pragun Kakkar'
email['to'] = 'kakkarpragun.work@gmail.com'
email['subject'] = 'Test email'

email.set_content("I am a python master")

try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('dummymailpragun@gmail.com', 'aldv sutq kklm ruvn')
        smtp.send_message(email)
        print('Email sent')
except smtplib.SMTPAuthenticationError as e:
    print("Failed to authenticate with the SMTP server.")
    print(f"Error code: {e.smtp_code}, Error message: {e.smtp_error}")
except Exception as e:
    print(f"An error occurred: {str(e)}")