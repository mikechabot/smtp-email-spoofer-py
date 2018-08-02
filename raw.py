import util

PORT_OUT_OF_RANGE = 'SMTP port is out-of-range (0-65535)'
PORT_NAN = 'SMTP port must be a number'


def get_port():
    while True:
        try:
            port = int(util.get_required_prompt('SMTP port: '))
            if port < 0:
                print(PORT_OUT_OF_RANGE)
            elif port > 65535:
                print(PORT_OUT_OF_RANGE)
            else:
                return str(port)
        except ValueError:
            print(PORT_NAN)


def get_debug_level():
    is_debug = util.get_optional_prompt('Enable debug (y/n)?: ', 'n')
    return util.convert_answer_to_int(is_debug)


def get_from_address():
    return util.get_required_prompt('\nEnter FROM address: ')


def get_from_name():
    return util.get_required_prompt('Enter FROM name (e.g. John Smith): ')


def get_subject():
    return util.get_required_prompt('Enter SUBJECT line: ')


def get_to_addresses():
    to_address = util.get_required_prompt('Enter TO address: ')
    to_addresses = [to_address]
    if is_multi_address():
        while to_address:
            to_address = util.get_optional_prompt('Enter TO address (blank to continue): ', None)
            if to_address:
                to_addresses.append(to_address)
    return to_addresses


def is_multi_address():
    is_multi = util.get_optional_prompt('Enter more TO addresses (y/n)?: ', 'n')
    return util.convert_answer_to_int(is_multi)


def load_body_from_file():
    load_from_file = util.get_optional_prompt('Load message body from file (y/n)?: ', 'n')
    return util.convert_answer_to_int(load_from_file)


def get_body_filename():
    return util.get_required_prompt('Filename: ')

