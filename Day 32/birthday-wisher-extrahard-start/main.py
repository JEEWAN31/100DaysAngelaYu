##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

from tkinter import *
import random
import pandas as pd
import smtplib as st
import datetime as dt

my_email = "jeewanjj02@gmail.com"
password = "tobpedizalgvnkpl"
now = dt.datetime.now()
df = pd.read_csv("birthdays.csv")
d = now.day
m = now.month
dic = df.to_dict("records")
print(dic)
name = ""
email = ""
ans = False
for item in dic:
    if item["month"] == m and item["day"] == d:
        name = item["name"]
        email = item["email"]
        ans = True
if ans:
    with st.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        x = random.randint(1,3)
        with open(f"letter_templates/letter_{x}.txt") as file:
            message = file.readline()
            message.replace("[NAME]", name)
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject:Hello I am jeewan \n\n {message}")
        print("Done")




