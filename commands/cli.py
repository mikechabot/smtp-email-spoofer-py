import logger
from smtpconnection import SMTPConnection

app_description = """  email-spoofer-py v0.0.2 (CLI wizard)  
  Python 3.x based email spoofer
  https://github.com/mikechabot/email-spoofer-py"""


def run(args):
    logger.bright('\n{0}'.format('='*50))
    logger.header(app_description)
    logger.bright('{0}\n'.format('='*50))

    # Connect to SMTP over TLS
    connection = SMTPConnection(args.host, str(args.port))

    # Attempt login
    if not args.noauth:
        success = connection.login(args.username, args.password)
        if success:
            logger.success('Authentication successful')
        else:
            exit(1)

    message_body = None
    with open(args.filename) as f:
        message_body = f.read()

    # Compose MIME message
    message = connection.compose_message(
        args.sender,
        args.name,
        args.recipients,
        args.subject,
        message_body
    )

    logger.bright('\n{0}\n'.format('='*70))
    logger.header(message.as_string())
    logger.bright('\n{0}\n'.format('='*70))

    connection.send_mail(message)

