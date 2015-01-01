#!/usr/bin/env python3

from io import TextIOWrapper, BytesIO
from subprocess import Popen, PIPE

"""Cleanly output anything with `less`

Most useful at the interpreter in combination with contextlib.redirect_stdout
>>> with Pager() as p:
...     with contextlib.redirect_stdout(p):
...        print("Print here as much as you like!")
...     p.display() # completely optional, will be called by __exit__ if not here
"""

__all__ = ['Pager']

class Pager(TextIOWrapper):
    def __init__(self):
        self.displayed = False
        super().__init__(BytesIO())

    def display(self):
        """Creates a subprocess to less, sending itself to stdin"""
        self.seek(0)
        with Popen(['less', '-'], stdin=PIPE) as process:
            process.communicate(self.buffer.getbuffer())
        self.displayed = True

    def __exit__(self, type, value, traceback):
        if not self.displayed:
            self.display()
        super().__exit__(type, value, traceback)
