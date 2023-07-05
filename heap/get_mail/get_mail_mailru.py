import imaplib
import email
import base64
from passwd.mailru import MAIL_PASS, USERNAME


mail_pass = MAIL_PASS
username = USERNAME
imap_server = 'imap.mail.ru'
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, mail_pass)
imap.select('SberBroker')

id_list = imap.search(None, 'ALL')[1][0].split()
for next_mail_id in id_list:
    res, data = imap.fetch(next_mail_id, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    payload = msg.get_payload()
    for part in msg.walk():
        if part.get_content_disposition() == 'attachment'\
                and part.get_filename()[-4:] == 'html'\
                and part.get_filename()[:7] == 'S03DNRY':
            with open(f'/home/stas/Загрузки/broker_report/{part.get_filename()}', 'w') as ouf:
                ouf.write(base64.b64decode(part.get_payload()).decode())
