import os
import sys
import time
import shutil
from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define categories and their corresponding folders
category_folders = {
    'anime': r'D:\MOVIEs\Anime',
    'movie': r'D:\MOVIEs\MOVIe',
    'series': r'D:\MOVIEs\SERIEs',
    'school stuff': r'D:\School',
    'books': r'D:\Books',
    'images': r'C:\Users\Admin\Pictures',
    'others': r'D:\Others'
}

class GoBackException(Exception):
    pass

def get_subfolder(category_folder):
    folder_stack = []
    while True:
        print("Choose a subfolder:")
        subfolders = [f.name for f in os.scandir(category_folder) if f.is_dir()]
        for i, subfolder in enumerate(subfolders, start=1):
            print(f"{i}. {subfolder}")
        print(f"{len(subfolders) + 1}. Create new subfolder")
        print(f"{len(subfolders) + 2}. Select this folder")
        print(f"{len(subfolders) + 3}. Go back")
        choice = input("Enter the number corresponding to your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(subfolders) + 3:
            if int(choice) == len(subfolders) + 1:
                while True:
                    new_subfolder = input("Enter the name of the new subfolder: ")
                    if new_subfolder in subfolders:
                        print("A subfolder with this name already exists. Please enter a different name.")
                    else:
                        return os.path.join(category_folder, new_subfolder)
            elif int(choice) == len(subfolders) + 2:
                return category_folder
            elif int(choice) == len(subfolders) + 3:
                if not folder_stack:
                    raise GoBackException
                else:
                    category_folder = folder_stack.pop()
            else:
                folder_stack.append(category_folder)
                category_folder = os.path.join(category_folder, subfolders[int(choice) - 1])
        else:
            print("Invalid choice. Please enter a number between 1 and", len(subfolders) + 3)

# Function to prompt user for category
def get_category():
    while True:
        print("Choose a category for the file:")
        for i, category in enumerate(category_folders.keys(), start=1):
            print(f"{i}. {category}")
        print(f"{len(category_folders) + 1}. Go back")
        choice = input("Enter the number corresponding to the category: ")
        if choice.isdigit() and 1 <= int(choice) <= len(category_folders) + 1:
            if int(choice) == len(category_folders) + 1:
                raise GoBackException
            return list(category_folders.keys())[int(choice) - 1]
        else:
            print("Invalid choice. Please enter a number between 1 and", len(category_folders) + 1)

# Function to move file to specified category folder
def organize_file(file_path, category):
    destination_folder = category_folders[category]
    destination_folder = get_subfolder(destination_folder)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    file_name = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, file_name)
    shutil.move(file_path, destination_path)
    print(f"File moved to {destination_folder}.")

def select_files(root, file_paths=None, use_terminal=False):
    try:
        if not use_terminal:
            if file_paths is None:
                file_paths = filedialog.askopenfilenames(parent=root)
        if not file_paths:
            return
        for file_path in root.tk.splitlist(file_paths):
            if not os.path.exists(file_path):
                print(f"File not found: {file_path}. Please select a valid file.")
                continue
            print(f"Processing file: {file_path}")
            while True:
                try:
                    category = get_category()
                    organize_file(file_path, category)
                    break
                except GoBackException:
                    print("Going back...")
            # Make the root window visible
                    
        if not use_terminal:
            root.deiconify()

            # Ask the user if they want to continue
            if messagebox.askyesno("Continue?", "Do you want to move another file?"):
                # Schedule the next file selection
                root.after(500, select_files, root)  # Try again after 0.5 seconds
            else:
                root.destroy()
    except Exception as e:
        print(f"An error occurred: {e}")
        root.destroy()

class DownloadHandler(FileSystemEventHandler):
    def __init__(self, root):
        self.root = root

    def on_modified(self, event):
        if not event.is_directory and event.event_type == "modified":
            time.sleep(10)
            print(f"Detected modified file: {event.src_path}")
            if not event.src_path.endswith(".tmp") and not event.src_path.endswith(".crdownload"):
                select_files(self.root, [event.src_path], use_terminal=True)

def main():
    # Create the root Tk window
    root = Tk()
    root.withdraw()

    # If the script was run with the argument "monitor", set up the watchdog observer
    if len(sys.argv) > 1 and sys.argv[1] == "monitor":
        event_handler = DownloadHandler(root)
        path = r'C:\Users\Admin\Downloads'
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            root.destroy()
            print("Observer stopped.")
        observer.join()
    else:
        # Otherwise, just open the file selection dialog
        select_files(root)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()