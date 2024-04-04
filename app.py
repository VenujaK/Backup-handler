from tkinter import *
from tkinter import filedialog
import os
import shutil


def get_user_input(message):
   

    while True:
        user_input = input(message)
        if user_input:
            return user_input
        else:
            print("Please enter a value.")


def create_folder(folder_path):
    

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def upload_with_backup(file_path, new_backup_folder, old_backup_folder):
   

    filename = os.path.basename(file_path)

    # Create new and old backup folders if they don't exist
    create_folder(new_backup_folder)
    create_folder(old_backup_folder)

    # Get existing file path in new backup folder
    old_file_path = os.path.join(new_backup_folder, filename)

    # Move existing file to old backup folder (always)
    if os.path.exists(old_file_path):
        shutil.move(old_file_path, os.path.join(old_backup_folder, filename))

    # Move uploaded file to new backup folder
    shutil.move(file_path, os.path.join(new_backup_folder, filename))

    print(f"File '{filename}' uploaded successfully! Backup stored in '{old_backup_folder}'.")


def upload_file():
   

    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    # Define new and old backup folder paths (modify as needed)
    new_backup_folder = "/Users/venujajayarathna/Documents/Web Backups/new_backup"
    old_backup_folder = "/Users/venujajayarathna/Documents/Web Backups/old_backup" 

    upload_with_backup(file_path, new_backup_folder, old_backup_folder)

    # Update success message
    success_label.config(text=f"File '{os.path.basename(file_path)}' uploaded successfully!")


# Create main window
root = Tk()
root.title("File Upload with Rotating Backups")

# File path label and entry
file_path_label = Label(root, text="File Path:")
file_path_label.pack()
file_path_entry = Entry(root)
file_path_entry.pack()
file_browse_button = Button(root, text="Browse", command=upload_file)
file_browse_button.pack()

# Success message label
success_label = Label(root, text="")
success_label.pack()

# Run the main loop
root.mainloop()