import smtplib
from email.mime.text import MIMEText
msg = MIMEText('My sample text for the email')
msg['Subject'] = 'The subject of email'
msg['From'] = 'rockybalboa@microsoft.com'
msg['To'] = 'rishap.sharma@enov8.com'
s = smtplib.SMTP('smtp-out.sapo.net.au')
s.sendmail('rockybalboa@microsoft.com', ['rishap.sharma@enov8.com'], msg.as_string())
s.quit()