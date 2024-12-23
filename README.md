# Easy Home Directory Backup

![A laptop sitting on a desk displaying the phrase "Easy Home Directory Backup" with a penguin sitting on the right side of the laptop.](easy_home_directory_backup_gemini_generated.jpeg)

A CLI program to perform either a full or partial backup of the user's Home Directory.

## Description

This Linux-only program runs in the user's Terminal to perform either a full or partial backup of the currently-logged
in user's Home Directory onto a local backup device.

## Getting Started

### Dependencies

* This program requires the latest version of Python.
* rsync
    * Some distributions already install this utility, but others may not. It can be downloaded from the distribution's
      package manager.
* tqdm
    * Download instructions for this program are present on the program's [repo](https://github.com/tqdm/tqdm). It is
      usually installed through `pip`, but other options are available.

### Installing

* To run the program you can do either of the following:
    * Clone the repo: https://github.com/brittbot-bgates/Easy-Home-Directory-Backup.git
    * Download the ZIP file from the
      repo: https://github.com/brittbot-bgates/Easy-Home-Directory-Backup/archive/refs/heads/main.zip

### Executing program

1. Open your Terminal
2. Change directory (`cd`) to the `src` directory of the program's directory path using one of the examples below:
    - Linux: `cd /home/$username/Downloads/Easy-Home-Directory-Backup/src`
3. Type the following command to run the program: `python main.py` or `python3 main.py`

## Help

* If you do you can reach out to me via one of the links in the [Author](#author) section.

## Author

* Brittany Gates
    * [Website](https://brittbot.com)
    * [Email](mailto:support@brittbot.com)
    * [LinkedIn](https://www.linkedin.com/in/brittanycgates/)
    * [Twitter / X](https://x.com/brittany__gates)
    * [YouTube](https://www.youtube.com/c/BrittanyGates)

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

* [Dominique Pizzie](https://gist.github.com/DomPizzie) for the simple README template
