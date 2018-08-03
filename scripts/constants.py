def _generate_fatal(message):
    return _generate_error(message) + ' Exiting...'


def _generate_error(message):
    return 'Error: ' + message


# SMTP strings
AUTH = 'auth'
STARTTLS = 'STARTTLS'
SUPPORTED_AUTH_TYPES = {'PLAIN', 'LOGIN'}

# Error strings
INVALID_HELO_REPLY = _generate_fatal('The server did not reply properly to the EHLO/HELO greeting.')
TLS_NOT_AVAILABLE = _generate_fatal('SSL/TLS support is not available to your Python interpreter.')
TLS_NOT_SUPPORTED = _generate_fatal('SMTP server does not support TLS.')
NO_SMTP_FEATURES = _generate_fatal('No SMTP features detected.')
NO_AUTH_FEATURES = _generate_fatal('No AUTH types detected.')
NO_PLAIN_OR_LOGIN_FEATURE = _generate_fatal('SMTP server does not support AUTH PLAIN or AUTH LOGIN.')
SOCKET_ERROR = _generate_fatal('Unable to establish connection to SMTP socket.')
UNABLE_TO_SEND_MESSAGE = _generate_fatal('Unable to send message. Check TO/FROM and Message body')

# Auth error strings
INVALID_CREDENTIALS = _generate_error('The server did not accept the username/password combination')
AUTH_NOT_SUPPORTED = _generate_fatal('The AUTH command is not supported by the server')
GENERIC_AUTHENTICATION_EXCEPTION = _generate_fatal('Encountered an error during authentication')

# General
COMMASPACE = ', '

