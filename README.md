# Downloads Folder Cleaner Script
This Python script organizes your `Downloads` folder by automatically sorting files into categorized folders based on their file types.

## 📝 Features

### Automatic Categorization:
 Sorts files into categories such as Images, Documents, Videos, Music, and more.

### Creates Folders:
 Automatically creates folders for each category if they don't exist.

### Handles Various File Types:
 Supports common file types like `.jpg`, `.pdf`, `.mp4`, `.exe`, and more.

### Error Handling: 
Gracefully handles any errors that occur during the file-moving process.

## 📁 File Categories
The following file categories are supported:

Images: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`

Documents: `.pdf`, `.docx`, `.doc`, `.txt`, `.pptx`, `.xlsx`, `.csv`

Videos: `.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`

Music: `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`

Archives: `.zip`, `.rar`, `.tar`, `.gz`, `.7z`

Executables: `.exe`, `.msi`, `.bat`

Installers: `.dmg`, `.pkg`

Code Files: `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.cs`

Others: Files that don't match any known category.

## 🚀 How to Use
### 1. Prerequisites

Ensure you have Python installed on your system. You can download it from python.org.

### 2. Running the Script

1. Save the script to a `.py` file, for example: `clean_downloads.py`

2. Open a terminal or command prompt.

3. Navigate to the script's location and run:
```
    python clean_downloads.py 
```

### 3. What It Does
Scans your `Downloads` folder.

Creates categorized folders if they don't already exist.

Moves files into the appropriate folders based on their file types.

Prints messages indicating the files being moved.

## ⚠️ Important Notes
### Backup: 
Always back up important files before running any script that manipulates your filesystem.

### Customization: 
You can customize the file categories by modifying the `FILE_CATEGORIES` dictionary in the script.

## 🛠️ Customizing the Script
You can add or modify categories by editing the `FILE_CATEGORIES` dictionary. For example:

```python
FILE_CATEGORIES = {
    "Images": [".jpg", ".png"],
    "Custom Category": [".xyz"]
}
```
## 📜 Sample Output

```
Moved 'photo.jpg' to 'Images' folder.
Moved 'report.pdf' to 'Documents' folder.
Moved 'song.mp3' to 'Music' folder.
Downloads folder cleaning complete!
```

## 🐞 Troubleshooting
### Permission Errors: 
Ensure you have the necessary permissions to move files in the Downloads directory.

### File in Use:
 Close any programs that may be using files in the Downloads folder before running the script.

### 🧹 Keep your Downloads folder organized and clutter-free!