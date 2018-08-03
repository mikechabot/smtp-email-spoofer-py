import smtplib
from socket import gaierror
from logger import info, success, error
from constants import \
    SOCKET_ERROR, STARTTLS, TLS_NOT_SUPPORTED, \
    TLS_NOT_AVAILABLE, INVALID_HELO_REPLY, NO_SMTP_FEATURES, \
    NO_AUTH_FEATURES, NO_PLAIN_OR_LOGIN_FEATURE, SUPPORTED_AUTH_TYPES, \
    INVALID_CREDENTIALS, AUTH_NOT_SUPPORTED, GENERIC_AUTHENTICATION_EXCEPTION, \
    UNABLE_TO_SEND_MESSAGE, COMMASPACE

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SMTPConnection:
    def __init__(self, host, port):
        self._host = host
        self._port  = port
        self._socket  = host + ':' + port
        self._server  = None
        self._sender = None
        self._recipients = None

        self.__connect()
        self.__start_tls()
        self.__eval_server_features()

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def server(self):
        return self._server

    @property
    def socket(self):
        return self._socket

    @property
    def sender(self):
        return self._sender

    @property
    def recipients(self):
        return self._recipients

    def __ehlo(self):
        try:
            self.server.ehlo()
        except smtplib.SMTPHeloError:
            error(INVALID_HELO_REPLY)
            exit(1)

    def __connect(self):
        try:
            info('Connecting to SMTP socket (' + self.socket + ')...')
            self._server = smtplib.SMTP(self.host, self.port)
            success('Connected to SMTP server')
        except (gaierror, OSError):
            error(SOCKET_ERROR)
            exit(1)

    def __start_tls(self):
        self.__ehlo()
        if not self.server.has_extn(STARTTLS):
            error(TLS_NOT_SUPPORTED)
            exit(1)
        else:
            try:
                info('Starting TLS session...')
                self.server.starttls()
                success('Started TLS session')
            except RuntimeError:
                error(TLS_NOT_AVAILABLE)
                exit(1)

    def __eval_server_features(self):
        self.__ehlo()
        features = self.server.esmtp_features;

        # Verify server features
        if not features:
            error(NO_SMTP_FEATURES)
            exit(1)

        # Verify auth feature
        auth_features = features['auth']
        if not auth_features:
            error(NO_AUTH_FEATURES)
            exit(1)

        # Verify auth types
        auth_types = []
        for auth_type in SUPPORTED_AUTH_TYPES:
            if auth_type in auth_features.strip().split():
                auth_types.append(auth_type)

        if not auth_types:
            error(NO_PLAIN_OR_LOGIN_FEATURE)
            exit(1)

    def login(self, username, password):
        try:
            self.server.login(username, password)
            success('Authentication successful')
            return True
        except smtplib.SMTPAuthenticationError:
            error(INVALID_CREDENTIALS)
            return False
        except smtplib.SMTPNotSupportedError:
            error(AUTH_NOT_SUPPORTED)
            exit(1)
        except smtplib.SMTPException:
            error(GENERIC_AUTHENTICATION_EXCEPTION)
            exit(1)

    def compose_message(self, sender, name, recipients, subject, html):
        self._sender = sender
        self._recipients = recipients

        message = MIMEMultipart('alternative')
        message.set_charset("utf-8")

        message["From"] = name + "<" + sender + ">"
        message['Subject'] = subject
        message["To"] = COMMASPACE.join(recipients)

        body = MIMEText(html, 'html')
        message.attach(body)
        return message;

    def send_mail(self, message):
        try:
            info('Sending spoofed message...')
            self.server.sendmail(self.sender, self.recipients, message.as_string())
            success('Sent message')
        except smtplib.SMTPException:
            error(UNABLE_TO_SEND_MESSAGE)
            exit(1)
