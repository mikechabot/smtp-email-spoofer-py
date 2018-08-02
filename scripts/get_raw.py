from scripts import util as u

PORT_OUT_OF_RANGE = 'SMTP port is out-of-range (0-65535)'
PORT_NAN = 'SMTP port must be a number'


def get_port():
    while True:
        try:
            port = int(u.get_required_prompt('SMTP port: '))
            if port < 0:
                print(PORT_OUT_OF_RANGE)
            elif port > 65535:
                print(PORT_OUT_OF_RANGE)
            else:
                return str(port)
        except ValueError:
            print(PORT_NAN)


def get_from_address():
    return u.get_required_prompt('Sender address (e.g. spoofed@domain.com): ')


def get_from_name():
    return u.get_required_prompt('Sender name (e.g. John Smith): ')


def get_subject():
    return u.get_required_prompt('Subject line: ')


def get_to_addresses():
    to_address = u.get_required_prompt('Recipient address (e.g. victim@domain.com): ')
    to_addresses = [to_address]
    if is_multi_address():
        while to_address:
            to_address = u.get_optional_prompt('Recipient address (blank to continue): ', None)
            if to_address:
                to_addresses.append(to_address)
    return to_addresses


def is_multi_address():
    is_multi = u.get_optional_prompt('Enter additional recipients (Y/N)?: ', 'N')
    return u.convert_answer_to_int(is_multi)


def load_body_from_file():
    load_from_file = u.get_optional_prompt('Load message body from file (Y/N)?: ', 'n')
    return u.convert_answer_to_int(load_from_file)


def get_body_filename():
    return u.get_required_prompt('Filename: ')


def do_send_mail():
    send_mail = u.get_required_prompt('Send message (Y/N)?: ')
    return u.convert_answer_to_int(send_mail)


