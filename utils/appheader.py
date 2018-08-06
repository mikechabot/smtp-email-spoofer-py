from logger import bright, header

description = """  email-spoofer-py v0.0.3 (CLI wizard)  
  Python 3.x based email spoofer
  https://github.com/mikechabot/email-spoofer-py"""

def print_header():
    bright('\n{0}'.format('='*50))
    header(description)
    bright('{0}\n'.format('='*50))


