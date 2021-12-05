import smtplib
import datetime as dt
import random
email = 'tonydavidmi@gmail.com'
password = 'opvomzekbduxzxjs'

with open('quotes.txt', 'r') as quotes_file:
    quotes = quotes_file.readlines()
now = dt.datetime.now()
today = now.weekday()

if today == 0:

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs='antonydavidmi@gmail.com',
            msg=f'Subject:Quotes of the day\n\n{random.choice(quotes)}',
        )
    print('Email sent')
