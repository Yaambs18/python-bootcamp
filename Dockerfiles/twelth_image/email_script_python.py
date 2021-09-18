import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
print(smtp_object.ehlo())
smtp_object.starttls()


email = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
print(smtp_object.login(email,password))

from_address = email
to_address = getpass.getpass("Enter the email of the recipient: ")

subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")

msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address,to_address,msg)

smtp_object.quit()
