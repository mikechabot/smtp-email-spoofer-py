import logger
import userinput as ui
from smtpconnection import SMTPConnection

app_description = """  email-spoofer-py v0.0.2 (CLI wizard)  
  Python 3.x based email spoofer
  https://github.com/mikechabot/email-spoofer-py"""


def run():
    logger.bright('\n{0}'.format('='*50))
    logger.header(app_description)
    logger.bright('{0}\n'.format('='*50))

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

    logger.bright('\n{0}\n'.format('='*70))
    logger.header(message.as_string())
    logger.bright('\n{0}\n'.format('='*70))

    if ui.do_send_mail():
        connection.send_mail(message)
