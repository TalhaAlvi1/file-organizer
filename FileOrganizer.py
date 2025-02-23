import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    file_categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'Scripts': ['.py', '.js', '.sh', '.bat'],
        'Executables': ['.exe', '.msi', '.dmg'],
        'Others': []
    }
    for category in file_categories.keys():
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False
            
            for category, extensions in file_categories.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(directory, category, file))
                    moved = True
                    break
            
            if not moved:
                shutil.move(file_path, os.path.join(directory, 'Others', file))

if __name__ == "__main__":
    target_directory = input("Enter the directory path to organize: ")
    organize_files(target_directory)
    print("Files have been organized successfully.")
