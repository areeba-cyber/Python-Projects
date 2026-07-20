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

    extension = os.path.splitext(file)[1].lower()

    moved = False

    for folder_name, extensions in file_types.items():

        if extension in extensions:

            destination = os.path.join(folder_path, folder_name)

            os.makedirs(destination, exist_ok=True)

            shutil.move(file_path, os.path.join(destination, file))

            print(f"{file} moved to {folder_name}")

            moved = True
            break


    if not moved:
        destination = os.path.join(folder_path, "Others")
        os.makedirs(destination, exist_ok=True)
        shutil.move(file_path, os.path.join(destination, file))
        print(f"{file} moved to Others")
print("\nFolder organized successfully!")