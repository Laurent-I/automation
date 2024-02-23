import os
import shutil
from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox

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

def get_subfolder(category_folder):
    while True:
        print("Choose a subfolder:")
        subfolders = [f.name for f in os.scandir(category_folder) if f.is_dir()]
        for i, subfolder in enumerate(subfolders, start=1):
            print(f"{i}. {subfolder}")
        print(f"{len(subfolders) + 1}. Create new subfolder")
        print(f"{len(subfolders) + 2}. Select this folder")
        choice = input("Enter the number corresponding to your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(subfolders) + 2:
            if int(choice) == len(subfolders) + 1:
                while True:
                    new_subfolder = input("Enter the name of the new subfolder: ")
                    if new_subfolder in subfolders:
                        print("A subfolder with this name already exists. Please enter a different name.")
                    else:
                        return os.path.join(category_folder, new_subfolder)
            elif int(choice) == len(subfolders) + 2:
                return category_folder
            else:
                category_folder = os.path.join(category_folder, subfolders[int(choice) - 1])
        else:
            print("Invalid choice. Please enter a number between 1 and", len(subfolders) + 2)

# Function to prompt user for category
def get_category():
    while True:
        print("Choose a category for the file:")
        for i, category in enumerate(category_folders.keys(), start=1):
            print(f"{i}. {category}")
        choice = input("Enter the number corresponding to the category: ")
        if choice.isdigit() and 1 <= int(choice) <= len(category_folders):
            return list(category_folders.keys())[int(choice) - 1]
        else:
            print("Invalid choice. Please enter a number between 1 and", len(category_folders))

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

def select_file(root):
    try:
        # Open the file dialog
        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        if not os.path.exists(file_path):
            print("File not found. Please select a valid file.")
            return
        category = get_category()
        organize_file(file_path, category)

        # Make the root window visible
        root.deiconify()

        # Ask the user if they want to continue
        if messagebox.askyesno("Continue?", "Do you want to move another file?"):
            # Schedule the next file selection
            root.after(500, select_file, root)  # Try again after 0.5 seconds
        else:
            root.destroy()
    except Exception as e:
        print(f"An error occurred: {e}")
        root.destroy()

# Main function
def main():
    # Create the root Tk window
    root = Tk()
    root.withdraw()

     # Start the file selection
    root.after(500, lambda: select_file(root))  # Start after 1 second

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()