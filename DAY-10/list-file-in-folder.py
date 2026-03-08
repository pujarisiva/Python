import os

def list_file_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except fileNotFoundError:
        return none, "Folder Not Found"
    except permissionError:
        return none, "Permission Denied"    

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces:").split()    
    for folder_path in folder_paths:
        files, error_messages = list_file_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()