import os
import shutil

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
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    file_name = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, file_name)
    shutil.move(file_path, destination_path)
    print(f"File moved to {category} folder.")

# Main function
def main():
    while True:
        file_path = input("Enter the path of the file to organize (or 'exit' to quit): ")
        if file_path.lower() == 'exit':
            break
        if not os.path.exists(file_path):
            print("File not found. Please enter a valid file path.")
            continue
        category = get_category()
        organize_file(file_path, category)

if __name__ == "__main__":
    main()