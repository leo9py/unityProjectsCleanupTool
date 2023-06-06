import os
import send2trash

def get_folder_size(folder):
    total_size = 0

    for path, dirs, files in os.walk(folder):
        for f in files:
            file_path = os.path.join(path, f)
            total_size += os.path.getsize(file_path)

    return total_size

def move_folders_to_recycle_bin(directory):
    folders_to_remove = ["Logs", "Library", "obj"]
    folders_found = []

    total_size_saved = 0

    for root, dirs, file in os.walk(directory):
        for folder in dirs:
            if folder in folders_to_remove:
                folder_path = os.path.join(root, folder)
                folders_found.append(folder_path)
                total_size_saved += get_folder_size(folder_path)

    if not folders_found:
        print("No folders found to remove.")
        return

    print("Folders found:")
    for folder_path in folders_found:
        print(folder_path)

    size_saved_gb = total_size_saved / (1024 * 1024 * 1024)
    print(f"Total size saved: {size_saved_gb:.2f} GB")

    confirmation = input("Confirm removal of the above folders? (y/n): ")
    if confirmation.lower() == "y":
        for folder_path in folders_found:
            send2trash.send2trash(folder_path)
        print("Folders moved to recycle bin.")
    else:
        print("Removal canceled.")

# Specify the directory containing your Unity projects
directory_path = "X:\\Archive\\Unorganized 06-2023\\VRChat Projects"

move_folders_to_recycle_bin(directory_path)
