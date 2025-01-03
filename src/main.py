#!/usr/bin/env python3
"""Easy_Home_Directory_Backup
Creator: Brittany Gates (https://github.com/brittbot-bgates) | (https://www.linkedin.com/in/brittanycgates) |
(https://brittbot.com/)
About: A program to back up the Home Directory in various Linux distributions via a one-time manual backup, or through
automated backups at a specific date and time.
"""
from console import console, notification
from text_display_tools import clear_screen, sleep_print
import sys


def main_menu() -> None:
    """Displays the menu.
    :return: None
    """
    clear_screen()
    console.print()
    console.print("Easy Home Directory Backup", justify="center")
    console.print()
    console.print("0 - Exit Program", justify="center")
    console.print("1 - Run A One-Time Backup", justify="center")
    console.print()
    from one_time_backup import one_time_backup  # Placing the imports here to avoid a circular import error
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
            one_time_backup()
        else:
            console.print()
            console.print("!! Enter either 0 or 1 !!", style=notification, justify="center")
            console.print()
            console.print(" -- The menu will reappear in a few seconds -- ", style=notification, justify="center")
            sleep_print()
            clear_screen()
            main_menu()


if __name__ == '__main__':
    main_menu()
