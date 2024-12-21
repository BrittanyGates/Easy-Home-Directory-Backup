#!/usr/bin/env python3
from pathlib import Path
from text_display_tools import *
import os, stat, subprocess, sys


def validate_backup_path(device_path: str) -> bool:
    """Validates the path of the backup device provided by the user.
    :param device_path: The user-supplied path to the backup device.
    :return: True if the path is valid, but False if it's invalid.
    """
    path = Path(device_path)

    def check_backup_device_permissions(backup_path: Path) -> bool:
        """Checks if the user-supplied backup device for read and write permissions.
        :param backup_path: The user-supplied path to the backup device.
        :return: True if the device has both read and write permissions, but False if it doesn't.
        """
        path_stats = os.stat(backup_path)
        mode = path_stats.st_mode
        return bool(mode & stat.S_IRUSR) and bool(mode & stat.S_IWUSR)

    def check_backup_device_file_system(backup_path: Path) -> bool:
        """Checks if the user-supplied backup device has a Linux-compatible (and rsync-compatible) file system.
        :param backup_path: The user-supplied path to the backup device.
        :return: True if the device is compatible, but False if it isn't.
        """
        # Get the file system type using stat command
        output = subprocess.run(["stat", "-f", backup_path], capture_output=True, text=True)
        filtered_output = output.stdout.strip()
        # The code below does work on both Debian and RHEL distros.
        backup_device_file_system = filtered_output.split(" ")[14].rstrip("Block")[:-1]
        if backup_device_file_system in ["ext2/ext3", "ext2", "ext3", "ext4", "XFS", "ZFS"]:
            return True
        else:
            return False

    def check_if_backup_path_is_a_mount_point(backup_path: Path) -> bool:
        """Checks if the user-supplied backup device is a mount point (Ex: /dev/sd* or /var).
        :param backup_path: The user-supplied path to the backup device.
        :return: True if the path is a mount point, but False if it isn't.
        """
        if os.path.ismount(backup_path):
            return True
        else:
            return False

    # If the path is the user's Home Directory
    if str(path).startswith("~") or str(path) == os.path.expanduser("~"):
        print()
        print(center_text(f"Backup path {path} cannot be your Home Directory"))
        print(center_text("That's all right: You can enter a new path in a few seconds."))
        sleep_print()
        clear_screen()
        return False
    # If the path isn't valid
    elif not path.exists():
        print()
        print(center_text(f"Backup path {path} doesn't exist."))
        print(center_text("That's all right: You can enter a new path in a few seconds."))
        sleep_print()
        clear_screen()
        return False
    # If the path isn't a directory
    elif not path.is_dir():
        print()
        print(center_text(f"Backup path {path} isn't a directory."))
        print(center_text("That's all right: You can enter a new path in a few seconds."))
        sleep_print()
        clear_screen()
        return False
    # If the backup device doesn't have read/write permissions
    elif not check_backup_device_permissions(path):
        print()
        print(center_text(f"Backup path {path} doesn't have read/write permissions."))
        print(center_text("Please add the read/write permissions to the backup device and run this program again."))
        sleep_print()
        print()
        print(center_text("*" * 80))
        print(center_text("!! Program exited !!"))
        print(center_text("*" * 80))
        print()
        sys.exit()
    # If the backup path is a mount point or a critical system directory (/dev/sd* or /var)
    elif not check_if_backup_path_is_a_mount_point(path):
        print()
        print(center_text(f"Path {path} is either a mount point or a critical system directory."))
        print(center_text("Those cannot be used as a backup device."))
        sleep_print()
        clear_screen()
        return False
    # If the backup device doesn't have a Linux/rsync compatible file system
    elif not check_backup_device_file_system(path):
        print()
        print(center_text(f"Backup path {path} isn't a Linux-compatible file system."))
        print(center_text("That's all right: You can enter a new path in a few seconds."))
        sleep_print()
        clear_screen()
        return False
    else:
        return True
