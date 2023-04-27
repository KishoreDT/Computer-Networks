import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("kishorejorden@gmail.com", "kishore1746010")
message = "Message_you_need_to_send"
s.sendmail("kishorejorden@gmail.com", "kishorebb1746jorden@gmail.com", message)