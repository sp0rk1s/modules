# tools module main script


# importing modules

import threading
import time
import os


# initializing modules

pass


# classes

class Sequence:
    """
    # Sequence\n
    ## Features\n
    """
    process: str = "Loading..."
    subprocess: str = ""
    manual: bool = False
    right_side: bool = False
    _end_message: str = None
    _longest: int = 0
    _status: str = "running"
    _step: int = 0
    _steps: list = [
        "\033[31m*\033[91m*\033[31m* ",
        " \033[31m*\033[91m*\033[31m*",
        "  \033[31m*\033[91m*",
        " \033[31m*\033[91m*\033[31m*",
        "\033[31m*\033[91m*\033[31m* ",
        "\033[91m*\033[31m*  ",
    ]

    def __init__(
        self,
        process: str = "Loading...",
        subprocess: str = "",
        manual: bool = False,
        right_side: bool = False
    ):
        self.process = process
        self.subprocess = subprocess
        self.manual = manual
        self.right_side = right_side
        if not manual:
            thr = threading.Thread(target = self._loop)
            thr.start()

    def _print(self, endline: bool = False):
        if self.subprocess != "":
            subprocess = f"({self.subprocess})"
        if self.right_side:
            buffer = f"{self.process} \033[37m{subprocess}\033[0m".rjust(os.get_terminal_size().columns - 6) + "\033[0m[{steps[self._step]}\033[0m]"
        else:
            buffer = f"\033[0m[{self._steps[self._step]}\033[0m] {self.process} \033[37m{subprocess}\033[0m"
            self._longest = max(self._longest, len(buffer))
            buffer.ljust(self._longest)
        if endline:
            buffer += "\n"
        print(buffer, end = "\r", flush = True)

    def _loop(self):
        while self._end_type == None:
            self._print()
        if self._end_type == "ok":
            buffer = f"\033[0m[\033[32m  OK  \033[0m] {self._end_message}\033[0m"
        elif self._end_type == "info":
            buffer = f"\033[0m[\033[36m INFO \033[0m] {self._end_message}\033[0m"
        elif self._end_type == "warn":
            buffer = f"\033[0m[\033[33m WARN \033[0m] {self._end_message}\033[0m"
        elif self._end_type == "depend":
            buffer = f"\033[0m[\033[31mDEPEND\033[0m] {self._end_message}\033[0m"
        elif self._end_type == "failed":
            buffer = f"\033[0m[\033[31mFAILED\033[0m] {self._end_message}\033[0m"
        else:
            buffer = f"\033[0m[{self._end_type.center(6)}\033[0m] {self._end_message}\033[0m".ljust(longest)
        print(buffer, flush = True)
    
    def ok(self, message: str = None):
        self._end_type = "ok"
        self._end_message = message

    def info(self, message: str = None):
        self._end_type = "info"
        self._end_message = message

    def warn(self, message: str = None):
        self._end_type = "warn"
        self._end_message = message

    def depend(self, message: str = None):
        self._end_type = "depend"
        self._end_message = message

    def failed(self, message: str = None):
        self._end_type = "failed"
        self._end_message = message

def load(
        process: str = "Loading...",
        subprocess: str = None,
        color: bool = True
    ):
    """
    ## Starts a loading process!\n
    Use the returned sequence to end the process in a desired way.
    """
    sequence: Sequence = Sequence(process, subprocess = subprocess, color = color)
    return sequence