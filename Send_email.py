import smtplib

EMAIL_ADD = input("Enter your Email-Address  : ")

EMAIL_PASS = input("Enter your Password : ")

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADD,EMAIL_PASS)
    try:
        subject = input("Enter The subject : ")
        body = input("Enter the Body : ")
        receiver = input("Enter the Receiver :")

        msg = f'Subject: {subject} \n\n {body}'

        smtp.sendmail(EMAIL_ADD , receiver , msg)
        print("Email Sent!")
        
    except:
        print("Something went wrong! \nFollow the step carefully ")
        

    
