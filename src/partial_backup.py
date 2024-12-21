#!/usr/bin/env python3
from check_data_usage import *
from datetime import date
from pathlib import Path
from tqdm import tqdm
from text_display_tools import *
from validate_backup_device import validate_backup_path
import os, subprocess, sys


def determine_partial_backup_type() -> str:
    """Allows the user to choose what type of partial backup to perform.
    :return: None
    """
    print(center_text("Choose a partial backup option to perform:"))
    print()
    print(center_text("1 - All non-dot directories (Documents, Photos, etc.)"))
    print(center_text("2 - Only dot directories (.bashrc, .config, etc."))
    print()
    try:
        user_choice: str = input("Enter your choice here: ")
        if user_choice == "1":
            return "1"
        elif user_choice == "2":
            return "2"
        else:
            print()
            print(center_text("*" * 80))
            print(center_text("!! Enter either 0, 1, or 2 !!"))
            print()
            print(center_text(" -- The menu will reappear in a few seconds -- "))
            print(center_text("*" * 80))
            sleep_print()
            clear_screen()
            determine_partial_backup_type()
    except ValueError:
        print()
        print(center_text("*" * 80))
        print(center_text("!! Incorrect input !!"))
        print()
        print(center_text("-- The menu will reappear in a few seconds --"))
        print(center_text("*" * 80))
        sleep_print()
        clear_screen()
        determine_partial_backup_type()


def partial_backup() -> None:
    """Performs a partial backup of the Home Directory.
    :return: None
    """
    print()
    print(center_text("Enter 0 to exit without performing a backup."))
    print()
    print(center_text("What is the path of the backup device?"))
    print(center_text("Examples: /mnt/Backup_Disk or /backups"))
    print()

    try:
        device_path: str = input("Enter the full path here: ")
        path = Path(device_path)
        home_dir_path = os.path.expanduser("~")
        if device_path == "0":
            print()
            print(center_text("*" * 80))
            print(center_text("!! You exited the program !!"))
            print(center_text("*" * 80))
            print()
            sys.exit()
        else:
            # If the user-supplied backup device path is invalid
            if not validate_backup_path(device_path):
                partial_backup()
            else:
                check_free_space_for_backup(path, home_dir_path)
                if determine_partial_backup_type() == "1":
                    today_date: date = date.today()
                    formatted_today_date: str = today_date.strftime("%m-%d-%Y")
                    # Create a directory on the backup device named after the formatted today's date of the backup
                    backup_device_path: str = f"{path}/{formatted_today_date}"
                    print()
                    sleep_print()
                    # Progress bar from tqdm
                    for _ in tqdm(range(100), desc="Backup Progress", unit="GB"):
                        """rsync options
                        a = Archive
                        z = Compression
                        """
                        subprocess.run(["rsync", "-az", "--exclude=.*",
                                        f"--log-file={path}/easy_home_directory_backup_{formatted_today_date}_log_file",
                                        home_dir_path, backup_device_path])
                    print()
                    print(center_text(f"A log of this backup can be found on {path}"))
                    print()
                    sys.exit()
                elif determine_partial_backup_type() == "2":
                    today_date: date = date.today()
                    formatted_today_date: str = today_date.strftime("%m-%d-%Y")
                    # Create a directory on the backup device named after the formatted today's date of the backup
                    backup_device_path: str = f"{path}/{formatted_today_date}"
                    print()
                    sleep_print()
                    # Progress bar from tqdm
                    for _ in tqdm(range(100), desc="Backup Progress", unit="GB"):
                        """rsync options
                        a = Archive
                        z = Compression
                        """
                        subprocess.run(["rsync", "-az", "--exclude=* --include=.*",
                                        f"--log-file={path}/easy_home_directory_backup_{formatted_today_date}_log_file",
                                        home_dir_path, backup_device_path])
                    print()
                    print(center_text(f"A log of this backup can be found on {path}"))
                    print()
                    sys.exit()
    except ValueError:
        print()
        print(center_text("*" * 80))
        print(center_text("!! Incorrect input !!"))
        print()
        print(center_text("-- The menu will reappear in a few seconds --"))
        print(center_text("*" * 80))
        sleep_print()
        clear_screen()
        partial_backup()
    except (EOFError, KeyboardInterrupt):
        print()
        print()
        print(center_text("*" * 80))
        print(center_text(" -- Interrupt signal received --"))
        print(center_text("*" * 80))
        print()
