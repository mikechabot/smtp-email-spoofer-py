from colorama import Fore, Style
from scripts import logger as l


def prompt(text):
    try:
        print(Fore.WHITE, end='')
        return input(text).strip()
    except KeyboardInterrupt:
        l.error('\nInterrupt received. Exiting...')
        exit(1)
    finally:
        print(Style.RESET_ALL, end='')


def get_required_input(text):
    var = None
    while not var:
        var = prompt(text)
    return var


def get_optional_input(text, default_value):
    var = prompt(text)
    if var:
        return var
    else:
        return default_value
