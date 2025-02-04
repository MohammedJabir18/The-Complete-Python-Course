import os
import shutil

# Get the path from the user
path = input("Enter your path: ")
files = os.listdir(path)

# Define file categories and extensions
data = {
"Images": ["jpg", "png", "jpeg"],
"Videos": ["mp4"],
"Documents": ["docs", "pdf", "xlsx"],
"Audios": ["mp3"]
}

# Iterate through all files
for file in files:
    file_name, extension = os.path.splitext(file)
    extension = extension.strip(".").lower()  # Iterate through all files
    
    # Check each category
    for data_type, exts in data.items():
        if extension in exts:
            folder_path = os.path.join(path, data_type)

            # Create the directory if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)

            # Move the file into the respective folder
            shutil.move(
                os.path.join(path, file),
                os.path.join(folder_path, file)
            )
            break  # Exit the loop once moved


