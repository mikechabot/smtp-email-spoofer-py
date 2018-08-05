import sys
from setup import init

init()  # Add packages to PYTHONPATH

from args import config
from commands import cli, wizard

if __name__ == '__main__':
    arg_length = len(sys.argv)
    if arg_length == 1:
        config.parser.print_help()      # Print help
        exit(1)
    elif arg_length == 2:
        if 'wizard' in sys.argv:
            wizard.run()                # Run wizard
        elif 'cli' in sys.argv:
            config.cli.print_help()     # Print CLI help
            exit(1)
        else:
            config.parser.parse_args()  # Generate parser warning messages
    else:
        args = config.parser.parse_args()
        cli.run(args)                   # Run CLI
