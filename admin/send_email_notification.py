
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_notification(subject, body, to, gmail_user, gmail_pwd):
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        text = msg.as_string()
        server.sendmail(gmail_user, to, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email, error: ", str(e))

if __name__ == "__main__":
    subject = "System Alert"
    body = "This is a test email for system administration automation."
    to = "recipient@example.com"
    gmail_user = "your-email@gmail.com"
    gmail_pwd = "your-password"
    send_email_notification(subject, body, to, gmail_user, gmail_pwd)
