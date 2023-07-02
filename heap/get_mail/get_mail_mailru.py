import imaplib
import email
from email.header import decode_header
import base64
from bs4 import BeautifulSoup
import re


mail_pass = 'midgDSBD6mktmgbRkB7a'
username = 'vostrov_so@bk.ru'
imap_server = 'imap.mail.ru'
imap = imaplib.IMAP4_SSL(imap_server)
print(imap.login(username, mail_pass))
print(imap.list())
print(imap.select('INBOX'))
print(imap.search())