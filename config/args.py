import sys
import argparse

parser = argparse.ArgumentParser(description='Python 3.x based email spoofer', allow_abbrev=False)

# Allowed commands: "wizard" or "cli"
subparsers = parser.add_subparsers(title='commands', dest='command', help='Allowed commands')
subparsers.add_parser('wizard', help='Use the step-by-step wizard')

cli = subparsers.add_parser('cli', help='Pass arguments directly')
cli.add_argument('--host', dest='host', required=True, type=str, help='SMTP hostname')
cli.add_argument('--port', dest='port', required=True, type=int, help='SMTP port number')


# Mutually exclude "--noauth" and "--username"
noauth_or_username = cli.add_mutually_exclusive_group(required=True)
noauth_or_username.add_argument('--noauth', dest='noauth', action='store_true', help='Disable authentication check')
noauth_or_username.add_argument('--username', dest='username', type=str, help='SMTP username')

# Make password required if "--username" is present
cli.add_argument('--password', dest='password', required='--username' in sys.argv, type=str, help='SMTP password')

# Email composition arguments
cli.add_argument('--sender', dest='sender', required=True, type=str, help='Sender address (e.g. spoofed@domain.com)')
cli.add_argument('--name', dest='name', required=True, type=str, help='Sender name (e.g. John Smith)')
cli.add_argument('--recipients', dest='recipients', required=True, type=str, nargs='+', help='Recipient addresses (e.g. victim@domain.com)')
cli.add_argument('--subject', dest='subject', required=True, type=str, help='Subject line')
cli.add_argument('--filename', dest='filename', required=True, type=str, help='Message body filename')
