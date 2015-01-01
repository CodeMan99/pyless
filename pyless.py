#!/usr/bin/env python3

import sys
from io import TextIOWrapper, BytesIO
from subprocess import Popen, PIPE

"""Cleanly output anything with `less`

Most useful at the interpreter in combination with contextlib.redirect_stdout
>>> with Pager() as p:
...     with contextlib.redirect_stdout(p):
...        print("Print here as much as you like!")
...     p.display() # completely optional, will be called by __exit__ if not here
"""

__all__ = ['Pager', 'StdoutPager']

PAGER_COMMAND = ['more'] if sys.platform == "win32" else ['less', '-']
PAGER_USE_SHELL = sys.platform == "win32"

class Pager(TextIOWrapper):
    def __init__(self):
        super().__init__(BytesIO())
        self.displayed = False

    def display(self):
        """Creates a subprocess to less, sending itself to stdin"""
        self.seek(0)
        with Popen(PAGER_COMMAND, stdin=PIPE, shell=PAGER_USE_SHELL) as process:
            process.communicate(self.buffer.getbuffer())
        self.displayed = True

    def __exit__(self, type, value, traceback):
        if not self.displayed:
            self.display()
        super().__exit__(type, value, traceback)

class StdoutPager(Pager):
    def __init__(self):
        super().__init__()
        sys.stdout = self

    def __exit__(self, type, value, traceback):
        sys.stdout = sys.__stdout__
        super().__exit__(type, value, traceback)
