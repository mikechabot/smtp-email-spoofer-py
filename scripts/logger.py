from colorama import init, Fore, Style

init()

def header(line):
    print(Fore.LIGHTBLACK_EX + line + Style.RESET_ALL)


def info(line):
    print(Fore.LIGHTCYAN_EX + line + Style.RESET_ALL)


def success(line):
    print(Fore.LIGHTGREEN_EX + line + Style.RESET_ALL)


def error(line):
    print(Fore.LIGHTRED_EX + line + Style.RESET_ALL)


def bright(line):
    print(Fore.LIGHTMAGENTA_EX + line + Style.RESET_ALL)
