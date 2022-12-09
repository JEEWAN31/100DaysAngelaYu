# SMTP e-mail module to work as much as possible
import smtplib as st
import datetime as dt

# Simple mail transfer protocol
#
# my_email = "jeewanjj02@gmail.com"
# password = "tobpedizalgvnkpl"
#
# with st.SMTP("smtp.gmail.com") as connection:
#     # start transport layer security
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="jeewan.3108@gmail.com",
#                         msg="Subject:Hello I am jeewan \n\n This is a email by Jeewan")


# ##################################################################################
Date = dt.datetime.now()
hello = Date.year
day = Date.weekday
print(day)
date_of_birth = dt.datetime(year=2001, month=8,day =31)
print(date_of_birth)
