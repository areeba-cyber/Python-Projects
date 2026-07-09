import os
import shutil

# Folder to organize
folder_path = input("Enter folder path: ")
# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Python Files": [".py"],
    "Others": []
}
# Check if folder exists
if not os.path.exists(folder_path):
    print("Folder does not exist!")
    exit()
# Organize files
for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    # Ignore folders
    if os.path.isdir(file_path):
        continue