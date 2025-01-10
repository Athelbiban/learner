import imaplib
import email
import base64
import re

from get_directory import get_directory
from passwd.mailru import MAIL_PASS, USERNAME


def loader_mail_attachments(imap, directory, files_extension='.html'):

    id_list = imap.search(None, 'ALL')[1][0].split()
    for next_mail_id in id_list:

        res, data = imap.fetch(next_mail_id, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        for part in msg.walk():

            if part.get_content_disposition() == 'attachment'\
                    and part.get_filename()[:7] == 'S03DNRY'\
                    and (re.search(r'\.\w+$', part.get_filename()).group() == files_extension
                         or re.search(r'\.\w+$', part.get_filename()).group() == files_extension.upper()):

                with open(f'{directory}{part.get_filename()}', 'w', encoding='utf-8') as ouf:
                    ouf.write(base64.b64decode(part.get_payload()).decode())


def main():

    if MAIL_PASS:
        mail_pass = MAIL_PASS
    else:
        mail_pass = input('MAIL_PASS: ')

    if USERNAME:
        username = USERNAME
    else:
        username = input('USERNAME: ')

    directory = get_directory()
    imap_server = 'imap.mail.ru'
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, mail_pass)
    imap.select('SberBroker')
    loader_mail_attachments(imap, directory)


if __name__ == '__main__':
    main()
