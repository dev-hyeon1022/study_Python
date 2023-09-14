# https://hyunmin1906.tistory.com/276
import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "dlatngustest1234@gmail.com"
receiver_email = "hited0123@gmail.com"
password = "mebxxpqiodmhanpr"
message = "안녕하세요"


context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.encode("utf-8"))
