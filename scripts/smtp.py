import smtplib
from scripts import util as u, pretty_print as l
from socket import gaierror

AUTH = 'auth'
STARTTLS = 'STARTTLS'
SUPPORTED_AUTH_TYPES = {'PLAIN', 'LOGIN'}

# Error strings
TLS_NOT_SUPPORTED = u.generate_fatal('SMTP server does not support TLS.')
NO_SMTP_FEATURES = u.generate_fatal('No SMTP features detected.')
NO_AUTH_FEATURES = u.generate_fatal('No AUTH types detected.')
NO_PLAIN_OR_LOGIN_FEATURE = u.generate_fatal('SMTP server does not support AUTH PLAIN or AUTH LOGIN.')
UNABLE_TO_CONNECT = u.generate_fatal('Unable to establish connection to SMTP socket.')

INVALID_CREDENTIALS = u.generate_error('The server did not accept the username/password combination')
AUTH_NOT_SUPPORTED = u.generate_error('The AUTH command is not supported by the server')
GENERIC_AUTHENTICATION_EXCEPTION = u.generate_error('Encountered an error during authentication')


def connect(host, port):
    socket = host + ':' + port
    l.info(' > Attempting connection to SMTP socket (' + socket + ')...')
    try:
        server = smtplib.SMTP(host, port)
        l.success(' > Successfully connected to SMTP server!')
        return server
    except (gaierror, OSError):
        l.error(UNABLE_TO_CONNECT)
        exit(1)


def start_tls(server):
    server.ehlo()
    if not server.has_extn(STARTTLS):
        l.error(TLS_NOT_SUPPORTED)
        exit(1)
    else:
        server.starttls()


def verify_auth_feature(features):
    if not features:
        l.error(NO_SMTP_FEATURES)
        exit(1)
    elif not features[AUTH]:
        l.error(NO_AUTH_FEATURES)
        exit(1)


def verify_auth_types(features):
    server_auth_types = features[AUTH].strip().split()

    auth_types = []
    for auth_type in SUPPORTED_AUTH_TYPES:
        if auth_type in server_auth_types:
            auth_types.append(auth_type)

    if not auth_types:
        l.error(NO_PLAIN_OR_LOGIN_FEATURE)
        exit(1)


def evaluate_server(server):
    server.ehlo()
    verify_auth_feature(server.esmtp_features)
    verify_auth_types(server.esmtp_features)


def login(server):
    login_attempt = None
    while not login_attempt:
        try:
            username = u.get_required_prompt('Username: ')
            password = u.get_required_prompt('Password: ')
            login_attempt = server.login(username, password)
        except smtplib.SMTPAuthenticationError:
            l.error(INVALID_CREDENTIALS)
        except smtplib.SMTPNotSupportedError:
            l.error(AUTH_NOT_SUPPORTED)
        except smtplib.SMTPException:
            l.error(GENERIC_AUTHENTICATION_EXCEPTION)

    l.success(' > ' + login_attempt[1].decode())
