## File Organizer

### Overview

This Python script automates the organization of files within a specified directory by moving them into subfolders based on their file extensions. For example, all `.txt` files will be moved into a `txt` folder, `.pdf` files into a `pdf` folder, and so on. Files without an extension will be placed in a `miscellaneous` folder.

### Features

  * **Automatic Sorting**: Organizes files into distinct folders named after their extensions (e.g., `pdf/`, `jpg/`).
  * **Handles No Extension**: Files without an extension are moved to a `miscellaneous` folder.
  * **Error Handling**: Includes basic error handling for file operations, such as permission errors or files that cannot be moved.
  * **User Feedback**: Provides console output during the organization process, indicating which files are being processed and moved.

### Requirements

  * Python 3.x

### How to Use

1.  **Save the Script**: Save the provided code as a Python file (e.g., `organize_files.py`).

2.  **Modify the Target Directory**:
    Open the `organize_files.py` file and change the `file_location_path` variable to the absolute path of the directory you want to organize.

    ```python
    file_location_path = "/path/to/your/directory" # <-- Change this line
    ```

    For example, if you want to organize your Downloads folder, you might set it to:

    ```python
    file_location_path = "/home/your_username/Downloads"
    ```

    (Replace `/home/your_username/Downloads` with the actual path on your system).

3.  **Run the Script**:
    Open a terminal or command prompt, navigate to the directory where you saved the script, and run it using Python:

    ```bash
    python organize_files.py
    ```

### Example Workflow

Let's say your `Downloads` folder (`/home/root/Downloads`) contains the following files:

```
/home/hari/Downloads/
├── document.pdf
├── image.jpg
├── report.docx
├── program.exe
├── archive.zip
├── notes.txt
├── .hidden_file
└── no_extension_file
```

After running the script, the `Downloads` folder will be organized as follows:

```
/home/root/Downloads/
├── pdf/
│   └── document.pdf
├── jpg/
│   └── image.jpg
├── docx/
│   └── report.docx
├── exe/
│   └── program.exe
├── zip/
│   └── archive.zip
├── txt/
│   └── notes.txt
├── miscellaneous/
│   └── no_extension_file
└── .hidden_file  (Skipped if no extension, or moved to 'hidden_file' folder if treated as extension by system)
```
