
import pandas
import random
import datetime as dt
import smtplib

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv('./birthdays.csv')
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (
    index, data_row) in data.iterrows()}
print(birthdays_dict)

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    print('Today is a birthday!')
    with open(f'./letter_templates/letter_{random.randint(1,3)}.txt', 'r') as letters:
        letter = letters.read()
        letter = letter.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(user='', password='')
        smtp.sendmail(from_addr='',
                      to_addrs=birthday_person['email'],
                      msg='Subject: Happy Birthday!\n\n' + letter)
        print('Email sent!')
