from prompt import get_required_input, get_optional_input
from logger import info, success

EMPTY_STRING = ''
PORT_OUT_OF_RANGE = 'SMTP port is out-of-range (0-65535)'
PORT_NOT_A_NUMBER = 'SMTP port must be a number'

def get_host():
    return get_required_input('\nSMTP host: ')


def get_port():
    while True:
        try:
            port = int(get_required_input('SMTP port: '))
            if port < 0:
                print(PORT_OUT_OF_RANGE)
            elif port > 65535:
                print(PORT_OUT_OF_RANGE)
            else:
                return str(port)
        except ValueError:
            print(PORT_NOT_A_NUMBER)


def get_username():
    return get_required_input('Username: ')


def get_password():
    return get_required_input('Password: ')


def get_sender_address():
    return get_required_input('Sender address (e.g. spoofed@domain.com): ')


def get_sender_name():
    return get_required_input('Sender name (e.g. John Smith): ')


def get_subject():
    return get_required_input('Subject line: ')


def get_recipient_addresses():
    to_address = get_required_input('Recipient address (e.g. victim@domain.com): ')
    to_addresses = [to_address]
    if is_multi_address():
        while to_address:
            to_address = get_optional_input('Recipient address (blank to continue): ', None)
            if to_address:
                to_addresses.append(to_address)
    return to_addresses


def is_multi_address():
    is_multi = get_optional_input('Enter additional recipients (Y/N)?: ', 'N')
    return _convert_answer_to_int(is_multi)


def do_load_body_from_file():
    load_from_file = get_optional_input('Load message body from file (Y/N)?: ', 'n')
    return _convert_answer_to_int(load_from_file)


def get_body_filename():
    return get_required_input('Filename: ')


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
    html = EMPTY_STRING
    while True:
        try:
            line = input('| ')
            html += line + '\n'
        except EOFError:
            success('Captured HTML body')
            break
    return html


def do_send_mail():
    send_mail = get_required_input('Send message (Y/N)?: ')
    return _convert_answer_to_int(send_mail)


def _convert_answer_to_int(answer):
    if answer.lower() in {'y', 'ye', 'yes'}:
        return 1
    return 0



