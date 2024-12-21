#!/usr/bin/env python3
from time import sleep
import os


def center_text(text, width=None) -> None:
    """Centers the displayed text in the terminal window.

    :param text: The text displayed on the terminal window.
    :param width: The width of the end user's terminal window.
    :return: None
    """
    if width is None:
        width = os.get_terminal_size().columns
    return text.center(width)


def clear_screen() -> None:
    """Clears the terminal screen using the operating system-specific command.
    :return: None
    """
    os.system("cls" if os.name == "nt" else "clear")


def sleep_print() -> None:
    """introduces a four-second pause in between printing story lines.
    :return: None
    """
    sleep(4)
