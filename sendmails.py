#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import smtplib
from email.mime.text import MIMEText
from email.Header import Header

def smtpconnect():
    s.ehlo()
    s.starttls()
    s.login("dutt.department.it@gmail.com", "Q4fT1qOO")

def test_conn_open(conn):
    try:
        status = conn.noop()[0]
    except:  # smtplib.SMTPServerDisconnected
        status = -1
    return True if status == 250 else False

def sendmail(info_list):
    logf = open("mail_errors.log","w")
    msg = MIMEText('Здравствуйте! Ваша заявка принята, номер заявки: '+info_list[1]+'<br>'+info_list[2]+'<br>'+info_list[3]+'<br>'+info_list[4]+'<br>'+info_list[5]+'<br>'+info_list[6], "html", "utf-8")
    msg['Subject'] = Header("Заявка на обучение в ДЮТТ номер: " + info_list[1], "utf-8")
    msg['From'] = "dutt.department.it@gmail.com"
    msg['To'] = info_list[0]
    if not test_conn_open(s):
        smtpconnect()
    try:
        s.sendmail("dutt.department.it@gmail.com", info_list[0], msg.as_string())
        print('Sended to: {0}, ID: {1}'.format(str(info_list[0]), str(info_list[1])))
    except smtplib.SMTPException as e:
        print(e)


def main():
    #В файле нужно сделать смещение первой строки вниз на ячейку
    with open("recipients.csv", "rb") as csvfile:

        msg_reader = csv.reader(csvfile, delimiter='|')
        msg_reader.next()
        map(lambda x: sendmail(x), msg_reader)

if __name__ == "__main__":
    global s
    s = smtplib.SMTP("smtp.gmail.com")
    smtpconnect()
    main()
