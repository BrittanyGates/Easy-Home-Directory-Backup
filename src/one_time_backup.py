#!/usr/bin/env python3
"""This module performs the one-time backup."""
from console import console, notification
from main import main_menu
from text_display_tools import clear_screen, sleep_print


def one_time_backup() -> None:
    """Performs a manual one-time backup in the Home Directory.
    :return: None
    """
    console.print("Easy Home Directory Backup - Perform A One-Time Backup", justify="center")
    console.print()
    console.print("0 - Back To Main Menu", justify="center")
    console.print("1 - Full backup of your Home Directory", justify="center")
    console.print("2 - Partial backup of your Home Directory", justify="center")
    console.print()
    from full_backup import full_backup  # Placing the imports here to avoid a circular import error
    from partial_backup import partial_backup  # Placing the imports here to avoid a circular import error

    try:
        menu_choice: int = int(input("Enter your choice here: "))
    except ValueError:
        console.print()
        console.print("!! This menu only accepts numbers !!", style=notification, justify="center")
        console.print()
        console.print("-- The menu will reappear in a few seconds --", style=notification, justify="center")
        sleep_print()
        clear_screen()
        one_time_backup()
    except (EOFError, KeyboardInterrupt):
        console.print()
        console.print()
        console.print(" -- Interrupt signal received --", style=notification, justify="center")
        console.print()
    else:
        if menu_choice == 0:
            clear_screen()
            main_menu()
        elif menu_choice == 1:
            full_backup()
        elif menu_choice == 2:
            partial_backup()
        else:
            console.print()
            console.print("!! Enter either 0, 1, or 2 !!", style=notification, justify="center")
            console.print()
            console.print(" -- The menu will reappear in a few seconds -- ", style=notification, justify="center")
            sleep_print()
            clear_screen()
            one_time_backup()
