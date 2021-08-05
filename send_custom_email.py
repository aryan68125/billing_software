import smtplib
import config_bill_var
#https://myaccount.google.com/lesssecureapps go here and turn on less secure apps

Email_Address = config_bill_var.Email_Address_sender
Password = config_bill_var.Password_sender



def send_email():
    with smtplib.SMTP("smtp.gmail.com",587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(Email_Address,Password)
 
        subject = "Thank you for visiting test retail shop"

        body = config_bill_var.mail_body

        msg = f'Subject: {subject} \n\n {body}'

        smtp.sendmail(Email_Address, config_bill_var.reciever_email_address ,msg)

