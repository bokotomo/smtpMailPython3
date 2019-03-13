# -*- coding: utf-8 -*-
"""
RUN:
    python sendMail.py "mail@.com" "title" "こんにちは"
"""
import smtplib
import sys
from email.mime.text import MIMEText
from email.utils import formatdate
from env import mail_config as config

class Mailer:
    def __init__(self, host, port, mail, password):
        self.host = host
        self.port = port
        self.password = password
        self.mail = mail

    def __create_message(self, to, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.mail
        msg['To'] = to
        msg['Date'] = formatdate()
        return msg

    def send(self, to, title, body):
        msg = self.__create_message(to, title, body)

        smtpobj = smtplib.SMTP(self.host, self.port)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(self.mail, self.password)
        smtpobj.sendmail(self.mail, to, msg.as_string())
        smtpobj.close()

def main(args):
    if len(args) != 4:
        print('args error')
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
    mailer = Mailer(host, port, mail, password)
    mailer.send(to, title, body)

if __name__ == "__main__":
    main(sys.argv)

