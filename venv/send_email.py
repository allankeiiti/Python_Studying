import smtplib, os
from email.mime.text import MIMEText


def add():
  # conexão com os servidores do google
  smtp_ssl_host = 'smtp.gmail.com'
  smtp_ssl_port = 465
  # username ou email para logar no servidor
  # seu email e sua senha dentro das aspas
  username = ''
  password = ''

  # quem vai enviar o e-mail dentor da aspas
  from_addr = ''
  # para quem vai o email dentro das aspas
  to_addrs = ['']

  message = MIMEText('E AE VIADÃO')
  message['subject'] = 'EMAIL TESTE DO PYTHON'
  message['from'] = from_addr
  message['to'] = ', '.join(to_addrs)

  # conectaremos de forma segura usando SSL
  server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

  server.login(username, password)
  server.sendmail(from_addr, to_addrs, message.as_string())
  server.quit()


add()