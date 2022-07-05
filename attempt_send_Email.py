from email.message import EmailMessage 
from email.utils import formatdate
import mimetypes
from pathlib import Path
import smtplib
import os
msg = EmailMessage()
msg['Subject'] = 'Un Mail avec Python'
msg['From'] = 'jeremie <louisbalenciaga22@gmail.com>'
msg['To'] = ', '.join(['charles.lucas@efrei.net'])
msg["Date"] = formatdate(localtime=True)
msg.set_content("""\
Salut!
Ci joint le fichier demandé.
""")
#path= os.path.abspath(os.getcwd())
#cfile = path+"/ping.txt"
cfile = Path("ping.txt")
ctype, encoding = mimetypes.guess_type(cfile)
if ctype is None or encoding is not None:
    ctype = 'application/octet-stream'
maintype, subtype = ctype.split('/', 1)
msg.add_attachment(cfile.read_bytes(), maintype=maintype, subtype=subtype, filename=cfile.name)
#with smtplib.SMTP('smtp.toto.fr') as csmtp:
smtplib.SMTP('smtp.toto.fr').send_message(msg)

 

 

