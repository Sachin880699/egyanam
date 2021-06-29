import smtplib

sender_mail = 'sachin.pawar7802@gmail.com'
receivers_mail = ["sachinnihcas373@gmail.com"]
message = "Too many failed login attempts"
password = "mymarathiamuchi"
smtpObj = smtplib.SMTP('gmail.com', 587)
smtpobj.login(sender_mail, password)
smtpObj.sendmail(sender_mail, receivers_mail, message)
