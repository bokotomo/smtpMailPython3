# -*- coding: utf-8 -*-
"""
RUN:
    python sendMail.py "mail@.com" "ok" "tomo"
"""
import smtplib
import sys
from email.mime.text import MIMEText
from email.utils import formatdate
from env import mail_config as config

class Mailer:
    def __init__(self, host, port, mail, password, to, title, body):
        self.host = host
        self.port = port
        self.password = password
        self.mail = mail
        self.to = to
        self.msg = self.create_message(title, body)

    def create_message(self, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.mail
        msg['To'] = self.to
        msg['Date'] = formatdate()
        return msg

    def send(self):
        smtpobj = smtplib.SMTP(self.host, self.port)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(self.mail, self.password)
        smtpobj.sendmail(self.mail, self.to, self.msg.as_string())
        smtpobj.close()

def main(args):
    if len(args) != 4:
        quit()
    # set args
    to = args[1]
    title = args[2]
    body = args[3]

    # set smtp
    mail = config.mail
    password = config.password
    port = config.port
    host = config.host

    # send mail
    mailer = Mailer(
        host,
        port,
        mail,
        password,
        to,
        title,
        body
    )
    mailer.send()

if __name__ == "__main__":
    main(sys.argv)

