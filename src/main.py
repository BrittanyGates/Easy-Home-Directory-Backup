#!/usr/bin/env python3
"""Easy Home Directory Backup
Creator: Brittany Gates (https://github.com/BrittanyGates) | (https://www.linkedin.com/in/brittanycgates) |
(https://brittbot.com/)
About: Perform one-time backups of the user's Home Directory for various Linux distributions.
"""
from console import console, notification
from text_display_tools import clear_screen, sleep_print
import sys


def main_menu() -> None:
    """Displays the main menu.
    :return: None
    """
    # Adding the imports here to avoid a circular import error
    from full_backup import full_backup
    from partial_backup import partial_backup
    clear_screen()
    console.print()
    console.print("Easy Home Directory Backup", justify="center")
    console.print()
    console.print("0 - Exit The Program", justify="center")
    console.print()
    console.print("1 - Perform A Full Backup", justify="center")
    console.print("Includes All Directories/Files", justify="center")
    console.print()
    console.print("2 - Perform A Partial Backup", justify="center")
    console.print("Excludes All Dot Directories/Files", justify="center")
    console.print()
    try:
        menu_choice: int = int(input("Enter your choice here: "))
    except ValueError:
        console.print()
        console.print("!! This menu only accepts numbers !!", style=notification, justify="center")
        console.print()
        console.print("-- The menu will reappear in a few seconds --", style=notification, justify="center")
        sleep_print()
        clear_screen()
        main_menu()
    except (EOFError, KeyboardInterrupt):
        console.print()
        console.print()
        console.print(" -- Interrupt signal received --", style=notification, justify="center")
        console.print()
    else:
        if menu_choice == 0:
            console.print()
            console.print("!! You exited the program !!", style=notification, justify="center")
            console.print()
            sys.exit()
        elif menu_choice == 1:
            clear_screen()
            full_backup()
        elif menu_choice == 2:
            clear_screen()
            partial_backup()
        else:
            console.print()
            console.print("!! Enter either 0, 1 or 2 !!", style=notification, justify="center")
            console.print()
            console.print(" -- The menu will reappear in a few seconds -- ", style=notification, justify="center")
            sleep_print()
            clear_screen()
            main_menu()


if __name__ == '__main__':
    main_menu()
