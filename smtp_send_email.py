# Python对SMTP支持有smtplib和email两个模块，
# email负责构造邮件，
# smtplib负责发送邮件。

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令:
from_addr = input('From: ')
authorization_code = input('Authorization Code: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
#smtp_server = input('SMTP server: ')
smtp_server = 'smtp.qq.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# server = smtplib.SMTP(smtp_server, 465)  # 使用SSL加密
server = smtplib.SMTP('smtp.qq.com', 587)  # 使用587端口
server.starttls()  # 启用TLS加密

server.set_debuglevel(1) # 打印出和SMTP服务器交互的所有信息
server.login(from_addr, authorization_code)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
