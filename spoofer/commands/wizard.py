from colorama import Fore
from getpass import getpass
from ..utils import logger, appdescription
from ..utils.userinput import prompt, get_required, get_optional, get_yes_no
from ..models.smtpconnection import SMTPConnection


def run(args):
    appdescription.print_description()

    host = get_required('SMTP host: ')
    port = None;

    while not port:
        try:
            port = int(get_required('SMTP port: '))
            if port < 0 or port > 65535:
                logger.error('SMTP port is out-of-range (0-65535)')
                port = None
        except ValueError:
            logger.error('SMTP port must be a number')
            port = None

    # Connect to SMTP over TLS
    connection = SMTPConnection(host, str(port))

    # Attempt login
    if not get_yes_no("Disable authentication (Y/N)?: ", 'n'):
        success = False
        while not success:
            success = connection.login(
                get_required('Username: '),
                getpass()
            )
        logger.success('Authentication successful')

    sender = get_required('Sender address: ')
    sender_name = get_required('Sender name: ');

    recipients = [get_required('Recipient address: ')]
    if get_yes_no('Enter additional recipients (Y/N)?: ', 'n'):
        while recipient:
            recipient = get_optional('Recipient address: ', None)
            if recipient:
                recipients.append(recipient)

    subject = get_required('Subject line: ')

    html = ''
    if get_yes_no('Load message body from file (Y/N)?: ', 'n'):
        filename = get_required('Filename: ')
        with open(filename) as f:
            html = f.read()
    else:
        logger.info('Enter HTML line by line')
        logger.info('To finish, press CTRL+D (*nix) or CTRL-Z (win) on an *empty* line')
        while True:
            try:
                line = prompt('>| ', Fore.LIGHTBLACK_EX)
                html += line + '\n'
            except EOFError:
                logger.success('Captured HTML body')
                break

    # Compose MIME message
    message = connection.compose_message(
        sender,
        sender_name,
        recipients,
        subject,
        html
    )

    if get_yes_no('Send message (Y/N)?: ', None):
        connection.send_mail(message)
