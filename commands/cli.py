import logger
from appheader import print_header
from smtpconnection import SMTPConnection


def run(args):
    print_header()

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

    connection.send_mail(message)

