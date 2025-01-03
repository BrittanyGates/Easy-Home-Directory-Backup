#!/usr/bin/env python3
"""This module performs the full backup."""
from check_data_usage import check_free_space_for_backup
from console import console, notification
from datetime import date
from pathlib import Path
from tqdm import tqdm
from text_display_tools import clear_screen, sleep_print
from validate_backup_device import validate_backup_path
import os, subprocess, sys


def full_backup() -> None:
    """Performs the full backup of the Home Directory.
    :return: None
    """
    console.print()
    console.print("Enter 0 to exit without performing a backup.", justify="center")
    console.print()
    console.print("What is the path of the backup device?", justify="center")
    console.print("Examples: /mnt/Backup_Disk or /backups", justify="center")
    console.print()
    try:
        device_path: str = input("Enter the full path here: ")
    except ValueError:
        console.print()
        console.print("!! Incorrect input !!", style=notification, justify="center")
        console.print()
        console.print("-- The menu will reappear in a few seconds --", style=notification, justify="center")
        sleep_print()
        clear_screen()
        full_backup()
    except (EOFError, KeyboardInterrupt):
        console.print()
        console.print()
        console.print(" -- Interrupt signal received --", style=notification, justify="center")
        console.print()
    else:
        path = Path(device_path)
        home_dir_path = os.path.expanduser("~")
        if device_path == "0":
            console.print()
            console.print("!! You exited the program !!", style=notification, justify="center")
            console.print()
            sys.exit()
        else:
            # If the user-supplied backup device path is invalid
            if not validate_backup_path(device_path):
                full_backup()
            else:
                check_free_space_for_backup(path, home_dir_path)
                today_date: date = date.today()
                formatted_today_date: str = today_date.strftime("%m-%d-%Y")
                # Create a directory on the backup device named after the formatted today's date of the backup
                backup_device_path: str = f"{path}/{formatted_today_date}"
                console.print()
                sleep_print()
                # Progress bar from tqdm
                for _ in tqdm(range(100), desc="Backup Progress", unit="GB"):
                    """rsync options
                    a = Archive
                    z = Compression
                    """
                    subprocess.run(["rsync", "-anz",
                                    f"--log-file={path}/easy_home_directory_backup_{formatted_today_date}_log_file",
                                    home_dir_path, backup_device_path])
                console.print()
                console.print(f"A log of this backup can be found on {path}", justify="center")
                console.print()
                sys.exit()
