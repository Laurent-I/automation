# Automation Scripts

This repository contains scripts that automate the process of organizing your files into different categories. The scripts are designed to make your life easier by automatically moving files to specified folders based on the category you choose.

## How it Works

The script monitors a specified directory for any file modifications. When a file is modified, the script prompts you to select a category for the file. The categories and their corresponding folders are defined in the `category_folders` dictionary at the beginning of the script. You can customize this dictionary to suit your needs.

Once you've chosen a category, the script will ask you to choose a subfolder within the category folder. You can either choose an existing subfolder, create a new one, or select the category folder itself. The script will then move the file to the chosen folder.

## Usage

You can run the script in two modes:

1. **Monitor mode:** In this mode, the script continuously monitors a specified directory for file modifications. To run the script in monitor mode, use the command `python organizer.py monitor`.

2. **Single run mode:** In this mode, the script will prompt you to select files to move, and then exit. To run the script in single run mode, use the command `python organizer.py`.

In both modes, the script will prompt you to choose a category and a subfolder for each file.

## Requirements

The script requires Python 3 and the following Python packages:

- `os`
- `sys`
- `time`
- `shutil`
- `tkinter`
- `watchdog`

You can install the required packages using pip:

```bash
pip install watchdog colorama
```
**Note:** The other packages are part of the Python Standard Library and should be available by default.

## Customization
You can customize the script to suit your needs by modifying the `category_folders` dictionary. The keys of the dictionary are the names of the categories, and the values are the paths to the corresponding folders.

For example, you could add a new category like this:

```bash
category_folders = {
    'anime': r'D:\MOVIEs\Anime',
    'movie': r'D:\MOVIEs\MOVIe',
    'series': r'D:\MOVIEs\SERIEs',
    'school stuff': r'D:\School',
    'books': r'D:\Books',
    'images': r'C:\Users\Admin\Pictures',
    'others': r'D:\Others',
    'my category': r'D:\MyCategory'  // Add your own category here
}
```
You can also change the directory that the script monitors by modifying the `path` variable in the `main` function. By default, the script monitors the 'Downloads' directory.

## Limitations

The script currently only supports moving files, not directories. If you want to move a directory, you will need to do it manually.