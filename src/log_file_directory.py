#!/usr/bin/env python3
"""This module creates the directory containing the log files."""
import os


def make_log_file_directory() -> None:
    """Creates the directory containing the log files.
    :return: None
    """
    home_dir_shortcut = os.path.expanduser("~")
    try:
        os.mkdir(f"{home_dir_shortcut}/.easy_home_directory_backup")
    except FileExistsError:
        pass
