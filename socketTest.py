from email.mime.text import MIMEText
import smtplib

# s = socket(AF_INET, SOCK_STREAM)
# s.connect(('www.sina.com.cn', 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
# buffer = d = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# print(data)
# s.close()

msg = MIMEText('hello, send by python')
fromAdr = 'imchensl@163.com'
fromPass = '!QAZxsw2'
toAdr = 'imzhangl@126.com'

stmpServer = 'smtp.163.com'

server = smtplib.SMTP(stmpServer, 25)
server.set_debuglevel(1)
server.login(fromAdr, fromPass)
server.sendmail(fromAdr, [toAdr], msg.as_string())
server.quit()
