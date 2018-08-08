from colorama import Fore, Style
from . import logger


def prompt(text, color):
    try:
        print(color, end='')
        return input(text).strip()
    except KeyboardInterrupt:
        logger.error('\nInterrupt received. Exiting...')
        exit(1)
    finally:
        print(Style.RESET_ALL, end='')


def get_required(text):
    var = None
    while not var:
        var = prompt(text, Fore.WHITE)
    return var


def get_optional(text, default_value):
    var = prompt(text, Fore.WHITE)
    if var:
        return var
    else:
        return default_value


def get_yes_no(text, default_value):
    if not default_value:
        val = get_required(text)
    else:
        val = get_optional(text, default_value)
    return _convert_answer_to_int(val)


def _convert_answer_to_int(answer):
    if answer.lower() in {'y', 'ye', 'yes'}:
        return 1
    return 0



