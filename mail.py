import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("mail id ", "16-digit password app password ")
message = "hello how r you"
s.sendmail("sender mail id", "receiver mail id ", message)
s.quit()
