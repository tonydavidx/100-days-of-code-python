import smtplib
import datetime as dt
import random
email = 'tonydavidmi@gmail.com'
password = 'opvomzekbduxzxjs'


with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(
        from_addr=email,
        to_addrs='antonydavidmi@gmail.com',
        msg='Hello!',
    )
print('Email sent')
