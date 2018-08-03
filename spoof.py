import os
import sys

# Append the scripts package to PYTHONPATH
base_dir = os.path.dirname(__file__) or '.'
scripts_package = os.path.join(base_dir, 'scripts')
sys.path.insert(0, scripts_package)

from scripts import *

header('==================================================')
header('  email-spoofer-py v0.0.2                         ')
header('  Python 3.x based email spoofer                  ')
header('  https://github.com/mikechabot/email-spoofer-py  ')
header('==================================================')

smtp_host = get_host()
smtp_port = get_port()

smtp = SMTPConnection(smtp_host, smtp_port) # Connect to SMTP over TLS

success = False
while not success:
    username = get_username()
    password = get_password()
    success = smtp.login(username, password)  # Attempt login

sender = get_sender_address()
name = get_sender_name()
recipients = get_recipient_addresses()
subject = get_subject()
message_html = get_message_body()

message = smtp.compose_message(sender, name, recipients, subject, message_html) # Compose MIME message

bright('\n===================================================================\n')
header(message.as_string())
bright('\n===================================================================\n')

if do_send_mail():
    smtp.send_mail(message)
