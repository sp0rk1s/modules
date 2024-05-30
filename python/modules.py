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
        if self._status == "loading":
            buffer = f"{self._steps[self._step]}\033[0m"
        elif self._status == "ok":
            buffer = f"\033[32m  OK  \033[0m"
        elif self._status == "info":
            buffer = f"\033[36m INFO \033[0m"
        elif self._status == "warn":
            buffer = f"\033[33m WARN \033[0m"
        elif self._status == "depend":
            buffer = f"\033[31mDEPEND\033[0m"
        elif self._status == "failed":
            buffer = f"\033[31mFAILED\033[0m"
        else:
            buffer = f"{self._end_type.center(6)}"
        if self.right_side:
            buffer = f"{self.process} \033[37m{subprocess}".rjust(os.get_terminal_size().columns - 8) + f"\033[0m[{buffer}]"
        else:
            buffer = f"\033[0m[{buffer}\033[0m] {self.process} \033[37m{subprocess}\033[0m"
            self._longest = max(self._longest, len(buffer))
            buffer.ljust(self._longest)
        if endline:
            print(buffer, flush = True)
        else:
            print(buffer, end = "\r", flush = True)

    def _loop(self):
        while self._status == "loading":
            self._print()
            time.sleep(0.15)
        self._print(endline = True)
    
    def end(self, message: str = "Finished loading.", type: str = "ok"):
        self._end_message = message
        self._status = type