from colorama import init
init()

AFFIRMATIVE_RESPONSES = {'y', 'ye', 'yes'}
ERROR = 'Error: '
EXITING = ' Exiting...'
EMPTY_STRING = ''
COMMASPACE = ', '


def prompt(text):
    return input(text).strip()


def get_required_prompt(text):
    var = None
    while not var:
        var = prompt(text)
    return var


def get_optional_prompt(text, default_value):
    var = prompt(text)
    if var:
        return var
    else:
        return default_value


def convert_answer_to_int(answer):
    if answer in AFFIRMATIVE_RESPONSES:
        return 1
    return 0


def generate_fatal(message):
    return ERROR + message + EXITING
