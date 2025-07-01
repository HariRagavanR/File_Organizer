import shutil
from pathlib import Path

file_location_path = "/home/hari/Downloads"

def organize_files():
    source_path = Path(file_location_path)

    if not source_path.exists():
        print(f"The directory '{source_path}' does not exist.")
        return

    print(f"\n Organizing files in: {source_path}\n")
    files_moved = 0

    for item in source_path.iterdir():
        if item.is_file():
            extension = item.suffix.lower()

            if not extension:
                print(f"Skipping '{item.name}' (no extension)")
                continue

            print(f"Found file: {item.name} (Extension: {extension})")

            folder_name = extension[1:] if extension.startswith('.') else "miscellaneous"
            destination_folder = source_path / folder_name

            destination_folder.mkdir(parents=True, exist_ok=True)

            try:
                shutil.move(str(item), str(destination_folder))
                files_moved += 1
                print(f"Moved to: {destination_folder.name}/\n")
            except shutil.Error as e:
                print(f"Error moving '{item.name}': {e}")
            except OSError as e:
                print(f"OS error while moving '{item.name}': {e}")
            except Exception as e:
                print(f"Unexpected error for '{item.name}': {e}")

    if files_moved > 0:
        print(f"\n Successfully moved {files_moved} file(s).")
    else:
        print("\n No files were moved. Please check the directory and extensions.")

if __name__ == "__main__":
    organize_files()
    print("\n File organization complete.")
