import smtplib
from scripts import get_raw as r, smtp as s, util as u, pretty_print as p

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

p.header('==================================================')
p.header('  email-spoofer-py v0.0.2                         ')
p.header('  Python 3.x based email spoofer                  ')
p.header('  https://github.com/mikechabot/email-spoofer-py  ')
p.header('==================================================')

smtp_host = u.get_required_prompt('\nSMTP host: ')
smtp_port = r.get_port()

server = s.connect(smtp_host, smtp_port)

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
    p.info(' > Enter HTML line by line')
    p.info(' > To finish, press CTRL+D (*nix) or CTRL-Z (win) on an *empty* line')
    html = u.EMPTY_STRING
    while True:
        try:
            line = input(' | ')
            html += line + '\n'
        except EOFError:
            p.success(' > HTML captured.')
            break
    body = MIMEText(html, 'html')
    msg.attach(body)

p.info(' > Send from ' + from_address + ' as ' + from_name)
p.info(' > Send to ' + u.COMMASPACE.join(to_addresses))

if r.do_send_mail():
    try:
        p.info(' > Sending spoofed message...')
        server.sendmail(from_address, to_addresses, msg.as_string())
        p.success(' > Successfully sent message!')
    except smtplib.SMTPException:
        p.error(' > Error: Unable to send message. Check TO/FROM and Message body')
else:
    p.info(' > Send message cancelled')





