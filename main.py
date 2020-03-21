import smtplib
import config


def send_email(subject,msg):
    try:
      server= smtplib.SMTP('smtp.gmail.com:587')  #for Gmail
      server.ehlo()
      server.starttls()
      server.login(config.EMAIL_ADDRESS,config.PASSWORD)
      print("5")
      message= 'Subject: {}\n\n{}'.format(subject,msg)
      print("6")
      server.sendmail(config.EMAIL_ADDRESS,config.EMAIL_ADDRESS, message)
      server.quit()
      print("Email sent successfully")
    except:
      print("Email failed to send")


subject="Test"
message="Hi there, I'm sending this e-mail from Python"
send_email(subject, message)