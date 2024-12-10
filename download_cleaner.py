import os
import shutil
import os.path

DOWNLOADS_PATH = os.path.join(os.path.expanduser("~"), "Downloads")

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".msi", ".bat"],
    "Installers": [".dmg", ".pkg"],
    "Code Files": [".py", ".js", ".html", ".css", ".java", ".cpp", ".cs"],
    "Others": []
}

def create_category_folders():
    for category in FILE_CATEGORIES.keys():
        folder_path = os.path.join(DOWNLOADS_PATH, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def get_file_category(file_name):
    _, extension = os.path.splitext(file_name)
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def clean_downloads():
    create_category_folders()
    
    for item in os.listdir(DOWNLOADS_PATH):
        item_path = os.path.join(DOWNLOADS_PATH, item)
        
      
        if os.path.isdir(item_path):
            continue

      
        category = get_file_category(item)
        destination_folder = os.path.join(DOWNLOADS_PATH, category)
        
        try:
            shutil.move(item_path, destination_folder)
            print(f"Moved '{item}' to '{category}' folder.")
        except Exception as e:
            print(f"Failed to move '{item}': {e}")

if __name__ == "__main__":
    clean_downloads()
    print("Downloads folder cleaning complete!")
