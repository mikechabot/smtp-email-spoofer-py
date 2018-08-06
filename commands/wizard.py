import logger
import userinput as ui
from appheader import print_header
from smtpconnection import SMTPConnection


def run():
    print_header()

    # Connect to SMTP over TLS
    connection = SMTPConnection(ui.get_host(), ui.get_port())

    # Attempt login
    if not ui.do_disable_auth():
        success = False
        while not success:
            success = connection.login(ui.get_username(), ui.get_password())

        logger.success('Authentication successful')

    # Compose MIME message
    message = connection.compose_message(
        ui.get_sender_address(),
        ui.get_sender_name(),
        ui.get_recipient_addresses(),
        ui.get_subject(),
        ui.get_message_body()
    )

    if ui.do_send_mail():
        connection.send_mail(message)
