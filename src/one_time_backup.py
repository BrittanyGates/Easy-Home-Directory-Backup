#!/usr/bin/env python3
from main import main_menu
from text_display_tools import *


def one_time_backup() -> None:
    """Performs a manual one-time backup in the Home Directory.
    :return: None
    """
    print(center_text("-" * 80))
    print(center_text("Easy Home Directory Backup - Perform A One-Time Backup"))
    print(center_text("-" * 80))
    print(center_text("0 - Back To Main Menu"))
    print(center_text("1 - Full backup of your Home Directory"))
    print(center_text("2 - Partial backup of your Home Directory"))
    print()

    try:
        from full_backup import full_backup  # Placing the imports here to avoid a circular import error
        from partial_backup import partial_backup  # Placing the imports here to avoid a circular import error
        menu_choice: int = int(input("Enter your choice here: "))
        if menu_choice == 0:
            clear_screen()
            main_menu()
        elif menu_choice == 1:
            full_backup()
        elif menu_choice == 2:
            partial_backup()
        else:
            print()
            print(center_text("*" * 80))
            print(center_text("!! Enter either 0, 1, or 2 !!"))
            print()
            print(center_text(" -- The menu will reappear in a few seconds -- "))
            print(center_text("*" * 80))
            sleep_print()
            clear_screen()
            one_time_backup()
    except ValueError:
        print()
        print(center_text("*" * 80))
        print(center_text("!! This menu only accepts numbers !!"))
        print()
        print(center_text("-- The menu will reappear in a few seconds --"))
        print(center_text("*" * 80))
        sleep_print()
        clear_screen()
        one_time_backup()
    except (EOFError, KeyboardInterrupt):
        print()
        print()
        print(center_text("*" * 80))
        print(center_text(" -- Interrupt signal received --"))
        print(center_text("*" * 80))
        print()
