import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import os
from dotenv import load_dotenv


class Gmail:
    def __init__(self):
        self.login = os.environ.get('LOGIN')
        self.password = os.environ.get('PASSWORD')

    # Send mail function
    def send_mail(self, recipients: list, subject: str, message: str, gmail_smtp='smtp.gmail.com') -> None:
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        # Identify ourselves to smtp gmail client
        ms = smtplib.SMTP(gmail_smtp, 587)
        ms.ehlo()
        ms.starttls()  # Secure our email with tls encryption
        # Re-identify ourselves as an encrypted connection
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()

    # Recieve mail function
    def recieve_mail(self, header=None, gmail_imap='imap.gmail.com'):
        mail = imaplib.IMAP4_SSL(gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select('inbox')
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

        return email_message

def main():
    load_dotenv()
    subject = 'subject'
    recipients = ['test@test.ru', 'newtest@test.ru']
    message = 'message'
    mail = Gmail()
    mail.send_mail(recipients, subject, message)
    any_new_letter = mail.recieve_mail()


if __name__ == '__main__':
    main()
