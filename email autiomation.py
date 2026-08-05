#EMAIL AUTOMATION

import random
import math
import smtplib #simple mail transfer protocol libarary

digits="0123456789"
OTP=""#Empty String

for  i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"is your OTP"
msg=otp

s=smtplib.SMTP("smtp.gmailcom",587)
s.starttls()
s.login("kasa.chaithanyareddy@gmail.com","yjwr huzn qdih nyhl")
user="kasa.chaithanyareddy@gmail.com"

emailid=input("enter the mail which you want to send OTP:")
s.sendmail(user,emailid,msg)

while True:
    a=input("enter the otp")
    if a==OTP:
        print("OTP is correct")
        break
    else:
        print("OTP is incorrect")
