import os
import sys

folders = ['commands', 'config', 'models', 'utils']

def init():
    base_dir = os.path.dirname(__file__) or '.'
    for folder in folders:
        sys.path.insert(0, os.path.join(base_dir, folder))
