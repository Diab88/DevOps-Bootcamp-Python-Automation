import requests
import smtplib
import os
import paramiko

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_notification(email_msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
try:
   response= requests.get('Website link')
   if response.status_code == 200:
      print('Application is running successfully!')
   else:
       print('Application is down, fix it')
       msg = f'Application returned {response.status_code}'
       send_notification()

       #restart the application
       ssh = paramiko.SSHClient()
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(hostname='Ip-Adress', username='root', key_filename='/Users/diab/.ssh/id_rsa')
       stdin, stdout, stderr = ssh.exec_command('docker start')
       print(stdout.readline())
       ssh.close()
       print('application restarted')
except Exception as ex:
    print(f'connection error Happened: {ex}')
    msg = 'Application not accessible at all'
    send_notification(msg)
