import sys
from setup import init

init()

from config import args
from commands import cli, wizard

if __name__ == '__main__':
    arg_length = len(sys.argv)
    if arg_length == 1:
        args.parser.print_help()
        exit(1)
    elif arg_length == 2:
        if 'wizard' in sys.argv:
            wizard.run()
        elif 'cli' in sys.argv:
            args.cli.print_help()
            exit(1)
        else:
            args.parser.parse_args() # generate parser warning messages
    else:
        args = args.parser.parse_args()
        print(args)
        cli.run(args)
