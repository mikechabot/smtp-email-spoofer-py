# smtp-email-spoofer-py
Python 3.x based email spoofer 

> *For educational purposes only. Do not send to or from addresses that you do not own.* 

> Email spoofing is often used for spam campaigns and phishing attacks. If you use this tool inappropriately, you could violate of the [CAN-SPAM Act of 2003](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) and/or the [Computer Fraud and Abuse Act](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act). You'd also be committing [wire fraud](https://en.wikipedia.org/wiki/Mail_and_wire_fraud#Wire). **Use your head**.

----

## Table of Contents

- [Getting Started](#getting-started)
- [Commands](#commands)
  - [Wizard](#wizard)
  - [CLI](#cli)
- [Result](#result)

## <a id="getting-started">Getting Started</a>

1. `$ git clone https://github.com/mikechabot/email-spoofer-py.git`
3. Activate `virtualenv`
2. `$ pip install -r requirements.txt`
3. `$ python spoof.py`

## <a id="commands">Commands</a>

`email-spoofer-py` offers two global commands: [`wizard`](#wizard) and [`cli`](#cli):

```bash
$ py spoof.py -h
usage: spoof.py [-h] {wizard,cli} ...

Python 3.x based email spoofer

optional arguments:
  -h, --help    show this help message and exit

commands:
  {wizard,cli}  Allowed commands
    wizard      Use the step-by-step wizard
    cli         Pass arguments directly
```    

----

### <a id="wizard">Wizard</a>

Issue the `wizard` command to use the step-by-step wizard:

```
$ py spoof.py wizard
```

1. Enter the SMTP server information to establish a connection over TLS:

<img src='https://raw.githubusercontent.com/mikechabot/image-assets/master/email-spoofer-py-tls-session.png' alt='logo' aria-label='https://github.com/mikechabot/email-spoofer-py-tls-session' />

2. Optionally provide credentials to login to the SMTP server:

<img src='https://raw.githubusercontent.com/mikechabot/image-assets/master/email-spoofer-py-auth.png' alt='logo' aria-label='https://github.com/mikechabot/email-spoofer-py-auth' />

3. Compose the forged message:

> Load the HTML message body from a file, or compose it within the shell

<img src='https://raw.githubusercontent.com/mikechabot/image-assets/master/email-spoofer-py-compose-msg.png' alt='logo' aria-label='https://github.com/mikechabot/email-spoofer-py-compose-msg' />

4. Send the message:

<img src='https://raw.githubusercontent.com/mikechabot/image-assets/master/email-spoofer-py-send.png' alt='logo' aria-label='https://github.com/mikechabot/email-spoofer-py-send' />

----

### <a id="cli">CLI</a>

Issue the `cli -h` command to view the help:

```bash
$ py spoof.py cli -h
usage: spoof.py cli [-h] (--noauth | --username USERNAME)
                    [--password PASSWORD] --host HOST --port PORT --sender
                    SENDER --name NAME --recipients RECIPIENTS
                    [RECIPIENTS ...] --subject SUBJECT --filename FILENAME

optional arguments:
  -h, --help            show this help message and exit
  --noauth              Disable authentication check
  --username USERNAME   SMTP username
  --password PASSWORD   SMTP password (required with --username)

required arguments:
  --host HOST           SMTP hostname
  --port PORT           SMTP port number
  --sender SENDER       Sender address (e.g. spoofed@domain.com)
  --name NAME           Sender name (e.g. John Smith)
  --recipients RECIPIENTS [RECIPIENTS ...]
                        Recipient addresses (e.g. victim@domain.com ...)
  --subject SUBJECT     Subject line
  --filename FILENAME   Message body filename (e.g. example.html)
```

1. Issue the `cli` command along with the appropriate arguments:

> If `--noauth` is not specified, `--username` and `--password` are required.

<img src='https://raw.githubusercontent.com/mikechabot/image-assets/master/email-spoofer-py-cli.png' alt='logo' aria-label='https://github.com/mikechabot/email-spoofer-py-cli' />

----

## Result

<img src='https://raw.githubusercontent.com/mikechabot/image-assets/master/email-spoofer-py-result.png' alt='logo' aria-label='https://github.com/mikechabot/email-spoofer-py-result' />

