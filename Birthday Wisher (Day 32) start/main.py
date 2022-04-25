import smtplib
import random
import datetime as dt

my_email = "pythontesting246@gmail.com"
password = "Y6383*ZtT"

now = dt.datetime.now()
day = now.weekday()

if day == 0:
    with open("quotes.txt") as file:
        contents = file.readlines()
        quote = random.choice(contents)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pythontesting246@yahoo.com",
            msg=f"Subject: Motivational Quote\n\n{quote}")