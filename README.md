# Easy Home Directory Backup

![A laptop sitting on a desk displaying the phrase "Easy Home Directory Backup" with a penguin sitting on the right side of the laptop.](easy_home_directory_backup_gemini_generated.jpeg)

A CLI program to perform either a full or partial backup of the user's Home Directory.

## Description

This Linux-only program runs in the user's Terminal to perform either a full or partial backup of the currently-logged
in user's Home Directory onto a local backup device.

## Getting Started

### Dependencies

* Python 3 (latest release is recommended).
* Rich Python Package
    * This package can be installed for various operating systems from PyPi [here](https://pypi.org/project/rich/).
* rsync
    * Some distributions already install this utility, but others may not. It can be downloaded from the distribution's
      package manager.
* tqdm
    * Download instructions for this program are present on the program's [repo](https://github.com/tqdm/tqdm). It is
      usually installed through `pip`, but other options are available.

### Download Options

* Download the program via one of the two options below:
    * Clone the repo: https://github.com/brittbot-bgates/Easy-Home-Directory-Backup.git
    * Download the ZIP file from the
      repo: https://github.com/BrittanyGates/Easy-Home-Directory-Backup/archive/refs/heads/master.zip

### Executing The Program

> I recommend executing this program in a Python Virtual Environment (virtualenv) to install the dependencies easier.
>
> Learn more about virtualenvs, including how to create them, from
> the [official Python Documentation](https://docs.python.org/3/library/venv.html).

1. Open the Terminal
2. Change directory (`cd`) to the `src` directory of the program's directory path using the examples below:
    - `cd /home/$username/Downloads/Easy-Home-Directory-Backup-master/src`
3. Type the following command to run the program: `python main.py` or `python3 main.py`

## Help

Please file a new issue using the [Issues](https://github.com/BrittanyGates/Easy-Home-Directory-Backup/issues) tab on
the
repo.

## Author

* Brittany Gates
    * [Website](https://brittbot.com)
    * [Email](mailto:support@brittbot.com)
    * [LinkedIn](https://www.linkedin.com/in/brittanycgates/)
    * [Twitter / X](https://x.com/brittany__gates)
    * [YouTube](https://www.youtube.com/c/BrittanyGates)

## Version History

* Latest release notes as of January 2025
    * Refactored the project to use the Rich package to improve the text displayed on screen.
    * Corrected the logic for all the `try/except` statements.
    * Added and/or fixed docstrings in various modules.
* Latest release notes as of late December 2024.
    * Initial release

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

* [Dominique Pizzie](https://gist.github.com/DomPizzie) for the simple README template
