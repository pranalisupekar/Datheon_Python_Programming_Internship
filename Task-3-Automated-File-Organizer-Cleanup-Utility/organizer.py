
import os
import shutil

print("=" * 50)
print("   Automated File Organizer & Cleanup Utility")
print("=" * 50)

# File extension and category mapping
categories = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".md": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".csv": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",

    ".py": "Code",
    ".java": "Code",
    ".cpp": "Code",
    ".c": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code"
}

# Take folder path from user
folder_path = input("Enter folder path to organize: ").strip().strip('"')

# Check whether the folder exists
if not os.path.isdir(folder_path):
    print("\nError: Folder does not exist.")

else:
    # Create category folders
    folder_names = [
        "Documents", "Images", "Videos",
        "Archives", "Code", "Other"
    ]

    for folder_name in folder_names:
        category_path = os.path.join(folder_path, folder_name)

        try:
            os.makedirs(category_path, exist_ok=True)
        except PermissionError:
            print("Permission denied:", category_path)

    # Initialize counters
    total_files = 0
    moved_files = 0
    skipped_files = 0

    print("\nOrganizing files...\n")

    # Read files from the selected folder
    try:
        for file in os.scandir(folder_path):

            if not file.is_file():
                continue

            # Avoid organizing this script itself
            if file.name == os.path.basename(__file__):
                continue

            total_files += 1

            try:
                # Identify the file extension
                extension = os.path.splitext(file.name)[1].lower()

                # Find the category
                category = categories.get(extension, "Other")

                # Create the destination path
                destination_folder = os.path.join(
                    folder_path, category
                )

                destination_path = os.path.join(
                    destination_folder, file.name
                )

                # Handle duplicate filenames
                if os.path.exists(destination_path):
                    name, ext = os.path.splitext(file.name)
                    number = 1

                    while os.path.exists(
                        os.path.join(
                            destination_folder,
                            f"{name}_{number}{ext}"
                        )
                    ):
                        number += 1

                    destination_path = os.path.join(
                        destination_folder,
                        f"{name}_{number}{ext}"
                    )

                # Move the file safely
                shutil.move(file.path, destination_path)

                print(f"Moved: {file.name} -> {category}/")
                moved_files += 1

            except FileExistsError:
                print(f"File already exists: {file.name}")
                skipped_files += 1

            except PermissionError:
                print(f"Permission denied: {file.name}")
                skipped_files += 1

            except OSError as error:
                print(f"Could not move {file.name}: {error}")
                skipped_files += 1
    except PermissionError:
        print("Error: Permission denied while reading the selected folder.")

    # Display final summary
    print("\n" + "=" * 50)
    print("           ORGANIZATION SUMMARY")
    print("=" * 50)
    print("Total files checked :", total_files)
    print("Files moved         :", moved_files)
    print("Files skipped       :", skipped_files)
    print("=" * 50)
    print("File organization completed!")
