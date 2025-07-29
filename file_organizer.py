import os
import shutil
import logging

logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv'],
}

def get_category(file_extension):
    """Return category name based on file extension"""
    for category, extensions in FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return category
    return 'Others'

def organize_files(target_directory):
    """Organize files in the target directory into categorized subfolders."""
    try:
        if not os.path.isdir(target_directory):
            logging.error(f"Invalid directory: {target_directory}")
            print(f"Error: '{target_directory}' is not a valid directory.")
            return

        files_moved = 0

        for item in os.listdir(target_directory):
            item_path = os.path.join(target_directory, item)

            if os.path.isfile(item_path):
                _, ext = os.path.splitext(item)
                category = get_category(ext)
                category_folder = os.path.join(target_directory, category)

                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                    logging.info(f"Created folder: {category_folder}")

                destination = os.path.join(category_folder, item)

                try:
                    shutil.move(item_path, destination)
                    logging.info(f"Moved '{item}' to '{category}' folder.")
                    files_moved += 1
                except Exception as move_error:
                    logging.error(f"Failed to move '{item}': {move_error}")
        
        print(f"✅ Organization complete. {files_moved} files moved.")
        print("📄 Log saved to 'file_organizer.log'.")

    except Exception as error:
        logging.error(f"Unexpected error: {error}")
        print(f"❌ Unexpected error occurred: {error}")

if __name__ == "__main__":
    print("📁 Python File Organizer")
    directory = input("Enter the full path of the folder to organize: ").strip()
    organize_files(directory)