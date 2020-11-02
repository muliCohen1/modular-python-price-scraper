import smtplib
# 
def send(message, url):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('email@gmail.com', 'pass')
        if isinstance(message, list):
            subject = message[0] + " Price change!"
            body = message[0] +" new price is " + message[1] +'\n' + "Prior price was " + message[2] + '\n' + 'Get it here: \n' + url 
        else:
            subject = message
            body = message + ": " + url
            print(message)
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(
            'email@gmail.com',
            'email_dest@gmail.com',
            msg
        )
        print("email has been sent")
        server.quit()