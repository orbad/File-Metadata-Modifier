import os
import re
from datetime import datetime
import subprocess

def change_file_modification_date(file_path, new_date):
    """
    Change the file modification date using exiftool.
    """
    # Format the date for exiftool (YYYY:MM:DD HH:MM:SS)
    formatted_date = new_date.strftime('%Y:%m:%d %H:%M:%S')

    # Full path to exiftool.exe
    exiftool_path = r'path\to\exiftool.exe'  # Replace this with the correct full path

    # Use exiftool to set the new date
    subprocess.run([exiftool_path, f'-FileModifyDate={formatted_date}', file_path], check=True)

    # Clean up the "_original" file created by exiftool
    original_file = f"{file_path}_original"
    if os.path.exists(original_file):
        os.remove(original_file)

def process_files_in_directory(directory):
    """
    Process each file in the directory, parse the date from the filename,
    and change the last modified date to match the date in the filename.
    """
    # Regex pattern to match filenames like VID-YYYYMMDD-WAxxxx.mp4
    pattern = re.compile(r'IMG-(\d{4})(\d{2})(\d{2})-WA\d{4}\.jpg')

    for filename in os.listdir(directory):
        # Only process files matching the pattern
        match = pattern.match(filename)
        if match:
            # Extract year, month, and day from the filename
            year, month, day = match.groups()

            # Create a datetime object from the extracted date
            file_date = datetime(year=int(year), month=int(month), day=int(day))

            # Get the full file path
            file_path = os.path.join(directory, filename)

            print(f"Processing file: {filename}")
            print(f"Setting file modification date to: {file_date}")

            # Change the file's modification date
            change_file_modification_date(file_path, file_date)

if __name__ == "__main__":
    # Replace this with the directory path containing your files
    directory_path = r'path\to\mediafiles\directory'  # Use raw string to avoid escape sequence issues

    process_files_in_directory(directory_path)
