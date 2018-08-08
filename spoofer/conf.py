import sys
import argparse
from spoofer.commands import cli, wizard

parser = argparse.ArgumentParser(description='Python 3.x based email spoofer', allow_abbrev=False)

# Allowed commands: "wizard" or "cli"
subparsers = parser.add_subparsers(title='commands', dest='command', help='Allowed commands', required=True)
wizard_subparser = subparsers.add_parser('wizard', help='Use the step-by-step wizard')
wizard_subparser.set_defaults(func=wizard.run)

cli_subparser = subparsers.add_parser('cli', help='Pass arguments directly')
cli_subparser.set_defaults(func=cli.run)

# Mutually exclude "--noauth" and "--username"
noauth_or_username = cli_subparser.add_mutually_exclusive_group(required=True)
noauth_or_username.add_argument('--noauth', dest='noauth', action='store_true', help='Disable authentication check')
noauth_or_username.add_argument('--username', dest='username', type=str, help='SMTP username')

# Make password required if "--username" is present
cli_subparser.add_argument('--password', dest='password', required='--username' in sys.argv, type=str, help='SMTP password (required with --username)')

required = cli_subparser.add_argument_group('required arguments')
required.add_argument('--host', dest='host', required=True, type=str, help='SMTP hostname')
required.add_argument('--port', dest='port', type=int, required=True, help='SMTP port number')

# Email composition arguments
required.add_argument('--sender', dest='sender', required=True, type=str, help='Sender address (e.g. spoofed@domain.com)')
required.add_argument('--name', dest='name', required=True, type=str, help='Sender name (e.g. John Smith)')
required.add_argument('--recipients', dest='recipients', required=True, type=str, nargs='+', help='Recipient addresses (e.g. victim@domain.com ...)')
required.add_argument('--subject', dest='subject', required=True, type=str, help='Subject line')
required.add_argument('--filename', dest='filename', required=True, type=str, help='Message body filename (e.g. example.html)')
