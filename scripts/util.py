from colorama import Fore, Style

AFFIRMATIVE_RESPONSES = {'y', 'ye', 'yes'}
ERROR = 'Error: '
EXITING = ' Exiting...'
EMPTY_STRING = ''
COMMASPACE = ', '


def prompt(text):
    return input(text).strip()


def get_required_prompt(text):
    print(Fore.WHITE, end='')
    var = None
    while not var:
        var = prompt(text)
    print(Style.RESET_ALL, end='')
    return var


def get_optional_prompt(text, default_value):
    print(Fore.WHITE, end='')
    var = prompt(text)
    print(Style.RESET_ALL, end='')
    if var:
        return var
    else:
        return default_value


def convert_answer_to_int(answer):
    if answer.lower() in AFFIRMATIVE_RESPONSES:
        return 1
    return 0


def generate_error(message):
    return ' > ' + ERROR + message


def generate_fatal(message):
    return generate_error(message) + EXITING


