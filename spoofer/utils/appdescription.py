from . import logger

description = """  email-spoofer-py v0.0.3 (CLI wizard)  
  Python 3.x based email spoofer
  https://github.com/mikechabot/email-spoofer-py"""

def print_description():
    logger.bright('\n{0}'.format('='*50))
    logger.header(description)
    logger.bright('{0}\n'.format('='*50))


