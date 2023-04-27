import smtplib
server_name = "smtp.gmail.com"
port = 465
server = smtplib.SMTP_SSL(server_name, port)
sender_emailid = "kishorejorden@gmail.com"
receiver_emailid = "kishorebb1746@gmail.com"
message_content = "Hello How are you!"
password = "kishore1746010"
server.login(sender_emailid, password)
server.sendmail(sender_emailid, receiver_emailid, message_content)