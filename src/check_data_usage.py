#!/usr/bin/env python3
"""This module performs various disk storage checks on the backup device."""
from console import console, error_message
import shutil, sys


def check_free_space_on_backup_device(backup_path) -> tuple[int, int, int]:
    """Checks the amount of total, used, and free space on the backup device.
    :param backup_path: The user-supplied path to the backup device.
    :return: A named tuple of integers containing the total, used, and free disk usage in Gigabytes (GB).
    """
    total, used, free = shutil.disk_usage(backup_path)
    return total // (2 ** 30), used // (2 ** 30), free // (2 ** 30)


def check_home_directory_size(home_dir) -> tuple[int, int, int]:
    """Checks the total size of the user's Home Directory.
    :param home_dir: The user's Home Directory.
    :return: A named tuple of integers containing the total, used, and free disk usage in Gigabytes (GB).
    """
    total, used, free = shutil.disk_usage(home_dir)
    return total // (2 ** 30), used // (2 ** 30), free // (2 ** 30)


def check_free_space_for_backup(backup_path, home_dir) -> bool:
    """Checks if there is enough space on the backup device to hold the backup.
    :param backup_path: The user-supplied path to the backup device.
    :param home_dir: The user's Home Directory.
    :return: True if there is enough space to hold the backup, but False it there isn't.
    """
    bd_total, bd_used, bd_free = check_free_space_on_backup_device(backup_path)
    hd_total, hd_used, hd_free = check_home_directory_size(home_dir)
    console.print()
    console.print(f"{backup_path} free disk space available: {bd_free} GB", justify="center")
    console.print(f"Home Directory disk usage: {hd_used} GB", justify="center")
    console.print()
    if hd_used >= bd_free:
        console.print(f"{backup_path} doesn't have enough space to contain the backup.", style=error_message,
                      justify="center")
        console.print("Either perform a partial backup, or free up space on the backup device.", style=error_message,
                      justify="center")
        sys.exit()
    else:
        return True
