#!/usr/bin/env python3
"""Easy_Home_Directory_Backup
Creator: Brittany Gates (https://github.com/brittbot-bgates) | (https://www.linkedin.com/in/brittanycgates) |
(https://brittbot.com/)
About: A program to back up the Home Directory in various Linux distributions via a one-time manual backup, or through
automated backups at a specific date and time.
"""
from text_display_tools import *
import sys


def main_menu() -> None:
    """Displays the menu.
    :return: None
    """
    print(center_text("-" * 80))
    print(center_text("Easy Home Directory Backup"))
    print(center_text("-" * 80))
    print(center_text("0 - Exit Program"))
    print(center_text("1 - Run A One-Time Backup"))
    print()

    try:
        from one_time_backup import one_time_backup  # Placing the imports here to avoid a circular import error
        menu_choice: int = int(input("Enter your choice here: "))
        if menu_choice == 0:
            print()
            print(center_text("*" * 80))
            print(center_text("!! You exited the program !!"))
            print(center_text("*" * 80))
            print()
            sys.exit()
        elif menu_choice == 1:
            clear_screen()
            one_time_backup()
        else:
            print()
            print(center_text("*" * 80))
            print(center_text("!! Enter either 0 or 1 !!"))
            print()
            print(center_text(" -- The menu will reappear in a few seconds -- "))
            print(center_text("*" * 80))
            sleep_print()
            clear_screen()
            main_menu()
    except ValueError:
        print()
        print(center_text("*" * 80))
        print(center_text("!! This menu only accepts numbers !!"))
        print()
        print(center_text("-- The menu will reappear in a few seconds --"))
        print(center_text("*" * 80))
        sleep_print()
        clear_screen()
        main_menu()
    except (EOFError, KeyboardInterrupt):
        print()
        print()
        print(center_text("*" * 80))
        print(center_text(" -- Interrupt signal received --"))
        print(center_text("*" * 80))
        print()


if __name__ == '__main__':
    main_menu()
