#!/usr/bin/python

import os
import smtplib

def send_email(recipient, subject, body):
    gmail_user = os.environ.get('G_EM')
    gmail_password = os.environ.get('G_P')
    FROM = gmail_user
    TO = recipient
    SUBJECT = subject
    TEXT = body

    message = "\From: %s\nTo: %s\nSubject: %s\n\n%s" % (FROM, TO, SUBJECT, TEXT)

    server = smtplib.SMTP("smtp.gmail.com", 587) # or 465
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(FROM, TO, message)
    server.close()

def main():
    send_email(gmail_user, "test email boilerplate", "test body")

if __name__ == '__main__':
    main()
