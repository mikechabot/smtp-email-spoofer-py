from getpass import getpass
from colorama import Fore, Style
from logger import info, success, error


def __prompt(text, color):
    try:
        print(color, end='')
        return input(text).strip()
    except KeyboardInterrupt:
        error('\nInterrupt received. Exiting...')
        exit(1)
    finally:
        print(Style.RESET_ALL, end='')


def __get_required_input(text):
    var = None
    while not var:
        var = __prompt(text, Fore.WHITE)
    return var


def __get_optional_input(text, default_value):
    var = __prompt(text, Fore.WHITE)
    if var:
        return var
    else:
        return default_value


def get_host():
    return __get_required_input('SMTP host: ')


def get_port():
    while True:
        try:
            port = int(__get_required_input('SMTP port: '))
            if port < 0:
                error('SMTP port is out-of-range (0-65535)')
            elif port > 65535:
                error('SMTP port is out-of-range (0-65535)')
            else:
                return str(port)
        except ValueError:
            error('SMTP port must be a number')


def get_username():
    return __get_required_input('Username: ')


def do_disable_auth():
    do_disable = __get_optional_input('Disable authentication (Y/N)?: ', 'n')
    return _convert_answer_to_int(do_disable)


def get_password():
    return getpass()


def get_sender_address():
    return __get_required_input('Sender address: ')


def get_sender_name():
    return __get_required_input('Sender name: ')


def get_subject():
    return __get_required_input('Subject line: ')


def get_recipient_addresses():
    to_address = __get_required_input('Recipient address: ')
    to_addresses = [to_address]
    if is_multi_address():
        while to_address:
            to_address = __get_optional_input('Recipient address: ', None)
            if to_address:
                to_addresses.append(to_address)
    return to_addresses


def is_multi_address():
    is_multi = __get_optional_input('Enter additional recipients (Y/N)?: ', 'N')
    return _convert_answer_to_int(is_multi)


def do_load_body_from_file():
    load_from_file = __get_optional_input('Load message body from file (Y/N)?: ', 'n')
    return _convert_answer_to_int(load_from_file)


def get_body_filename():
    return __get_required_input('Filename: ')


def get_message_body():
    if do_load_body_from_file():
        filename = get_body_filename()
        with open(filename) as f:
            return f.read()
    else:
       return get_html()


def get_html():
    info('Enter HTML line by line')
    info('To finish, press CTRL+D (*nix) or CTRL-Z (win) on an *empty* line')
    html = ''
    while True:
        try:
            line = __prompt('>| ', Fore.LIGHTBLACK_EX)
            html += line + '\n'
        except EOFError:
            success('Captured HTML body')
            break
    return html


def do_send_mail():
    send_mail = __get_required_input('Send message (Y/N)?: ')
    return _convert_answer_to_int(send_mail)


def _convert_answer_to_int(answer):
    if answer.lower() in {'y', 'ye', 'yes'}:
        return 1
    return 0



