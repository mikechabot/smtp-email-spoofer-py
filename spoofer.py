import smtplib
import util as u
import raw as r
import smtp as s

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_host = u.get_required_prompt('SMTP server: ')
smtp_port = r.get_port()
debug_level = r.get_debug_level()

server = s.connect(smtp_host, smtp_port, debug_level)

s.start_tls(server)
s.evaluate_server(server)
s.login(server)

from_address = r.get_from_address()
from_name = r.get_from_name()
to_addresses = r.get_to_addresses()
subject = r.get_subject()

msg = MIMEMultipart('alternative')
msg.set_charset("utf-8")

msg["From"] = from_name + "<" + from_address + ">"
msg['Subject'] = subject
msg["To"] = u.COMMASPACE.join(to_addresses)

load_body_from_file = r.load_body_from_file()

if load_body_from_file:
    filename = r.get_body_filename()
    with open(filename) as file:
        body = MIMEText(file.read(), 'html')
        msg.attach(body)
else:
    print('--> Enter HTML line by line.')
    print('--> Press CTRL+D on an empty line to finish.)')
    html = u.EMPTY_STRING
    while True:
        try:
            line = input("> ")
            html += line + "\n"
        except EOFError:
            print('HTML captured.')
            break
    body = MIMEText(html, 'html')
    msg.attach(body)

print('\n--> Spoofing from ' + from_address + ' (' + from_name + ')')
print('--> Sending to ' + u.COMMASPACE.join(to_addresses))

try:
    server.sendmail(from_address, to_addresses, msg.as_string())
    print('\nSuccessfully sent email')
except smtplib.SMTPException:
    print('\nError sending email. Check FROM/TO and MESSAGE body.')
