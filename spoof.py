import sys
from spoofer import conf

def main():
    args = conf.parser.parse_args()
    args.func(args)

sys.exit(main())
