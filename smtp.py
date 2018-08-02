import smtplib
import util as u
from socket import gaierror

AUTH = 'auth'
STARTTLS = 'STARTTLS'
SUPPORTED_AUTH_TYPES = {'PLAIN', 'LOGIN'}

# Error strings
TLS_NOT_SUPPORTED = u.generate_fatal('SMTP server does not support TLS.')
NO_SMTP_FEATURES = u.generate_fatal('No SMTP features detected.')
NO_AUTH_FEATURES = u.generate_fatal('No AUTH types detected.')
NO_PLAIN_OR_LOGIN_FEATURE = u.generate_fatal('SMTP server does not support AUTH PLAIN or AUTH LOGIN.')
UNABLE_TO_CONNECT = u.generate_fatal('Unable to connect to SMTP server. Check hostname and port.')

INVALID_CREDENTIALS = 'Error: The server did not accept the username/password combination'
AUTH_NOT_SUPPORTED = 'Error: The AUTH command is not supported by the server'
GENERIC_AUTHENTICATION_EXCEPTION = 'Error: Encountered an error during authentication'


def connect(host, port, debug):
    socket = host + ':' + port
    print('\nAttempting connection to socket (' + socket + ')...')
    try:
        server = smtplib.SMTP(host, port)
        server.set_debuglevel(debug)
        print('--> Successfully connected to SMTP server!\n')
        return server
    except (gaierror, OSError):
        print(UNABLE_TO_CONNECT)
        exit(1)


def start_tls(server):
    server.ehlo()
    if not server.has_extn(STARTTLS):
        print(TLS_NOT_SUPPORTED)
        exit(1)
    else:
        server.starttls()


def verify_auth_feature(features):
    if not features:
        print(NO_SMTP_FEATURES)
        exit(1)
    elif not features[AUTH]:
        print(NO_AUTH_FEATURES)
        exit(1)


def get_supported_server_auth_types(features):
    server_auth_types = features[AUTH].strip().split()

    auth_types = []
    for auth_type in SUPPORTED_AUTH_TYPES:
        if auth_type in server_auth_types:
            auth_types.append(auth_type)

    if not auth_types:
        print(NO_PLAIN_OR_LOGIN_FEATURE)
        exit(1)
    else:
        return auth_types


def evaluate_server(server):
    server.ehlo()
    verify_auth_feature(server.esmtp_features)

    print('Listing supported AUTH types...')
    for auth_type in get_supported_server_auth_types(server.esmtp_features):
        print("--> " + auth_type)


def login(server):
    login_attempt = None
    while not login_attempt:
        try:
            username = u.get_required_prompt('\nEnter username: ')
            password = u.get_required_prompt('Enter password: ')
            login_attempt = server.login(username, password)
        except smtplib.SMTPAuthenticationError:
            print(INVALID_CREDENTIALS)
        except smtplib.SMTPNotSupportedError:
            print(AUTH_NOT_SUPPORTED)
        except smtplib.SMTPException:
            print(GENERIC_AUTHENTICATION_EXCEPTION)

    print('--> ' + login_attempt[1].decode())
