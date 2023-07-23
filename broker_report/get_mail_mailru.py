import imaplib
import email
import base64
import re
from passwd.mailru import MAIL_PASS, USERNAME

def loader_mail_attachments(imap, directory, files_extension='.html'):
    id_list = imap.search(None, 'ALL')[1][0].split()
    for next_mail_id in id_list:
        res, data = imap.fetch(next_mail_id, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        for part in msg.walk():
            if part.get_content_disposition() == 'attachment'\
                    and part.get_filename()[:7] == 'S03DNRY'\
                    and re.search(r'\.\w+$', part.get_filename()).group() == files_extension:
                with open(f'{directory}{part.get_filename()}', 'w') as ouf:
                    ouf.write(base64.b64decode(part.get_payload()).decode())


def main():
    mail_pass = input('MAIL_PASS: ')
    username = input('USERNAME: ')
    directory = '/home/stas/Загрузки/broker_report/'
    imap_server = 'imap.mail.ru'
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, mail_pass)
    imap.select('SberBroker')
    loader_mail_attachments(imap, directory)


if __name__ == '__main__':
    main()
