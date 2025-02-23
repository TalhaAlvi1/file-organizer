# File Organizer Script

This script organizes files in a specified directory by moving them into categorized subfolders based on their file extensions.

## How It Works
- The script scans the given directory for files.
- It moves files into predefined folders such as `Images`, `Documents`, `Audio`, `Videos`, `Archives`, `Scripts`, `Executables`, and `Others`.
- If a file's extension is not recognized, it is placed in the `Others` folder.

## Prerequisites
- Python installed on your system.

## Installation
1. Clone this repository or download the script.
2. Ensure Python is installed by running:
   ```sh
   python --version
   ```

## Usage
1. Open a terminal or command prompt.
2. Run the script using the following command:
   ```sh
   python FileOrganizer.py
   ```
3. Enter the directory path when prompted.
4. The script will organize the files into categorized folders.

## Example
```
Enter the directory path to organize: /Users/username/Downloads
Files have been organized successfully.
```

## Notes
- Ensure you have write permissions for the directory.
- The script will create new folders if they do not exist.

## License
This project is licensed under the MIT License.
