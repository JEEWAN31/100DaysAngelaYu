import datetime as dt
import smtplib as st
import random

my_email = "jeewanjj02@gmail.com"
password = "tobpedizalgvnkpl"

date = dt.datetime.now()
if date.weekday() == 4:
    with open("quotes.txt") as quote:
        all_quotes = quote.readlines()
        qu = random.choice(all_quotes)
    print(qu)

    with st.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password= password)
        connection.sendmail(from_addr=my_email, to_addrs="jeewan.3108@gmail.com",msg=f"Subject: Monday's motivation\n\n {qu}")



