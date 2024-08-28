import os
import shutil
import schedule
import time
import pandas as pd

#File organization
def organize_files_by_extension(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: The folder with '{folder_path}' as a path does not exist.")
        return 
    # Loop through each file in the directory
    for filename in os.listdir(folder_path):
        # Construct the absolute path of the file
        file_path = os.path.join(folder_path, filename)
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Extract file extension and define the destination subfolder
        file_extension = filename.split('.')[-1].lower()
        destination_folder = os.path.join(folder_path, file_extension)

        # Create the destination subfolder if it does not exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Relocate the file to its new subfolder
        shutil.move(file_path, destination_folder)

        print(f'Moved: {filename} to {destination_folder}/')


#Backup automation
def backup_data(src_dir,backup_dir):
    # Create a timestamped backup directory for understanding when it was taken
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') # get the current date and time converted to string
    backup_directory = os.path.join(backup_dir + timestamp)
    
    try:
        # Copy the source directory to the backup directory
        shutil.copytree(src_dir, backup_dir)
        print(f"Backup successful to {backup_directory}")
    except Exception as e:
        print(f"Backup Failed! Error: {str(e)}")

#Restore data
def restore_data(backup_dir,restore_dir):
    try:
        # Copy the backup directory to the restore directory
        shutil.copytree(backup_dir, restore_dir)
        print(f"Data restored to {restore_dir}")
    except Exception as e:
        print(f"Data Restore Failed! Error: {str(e)}")

