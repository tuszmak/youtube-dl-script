import os
import re

def clean_filename(filename_to_clean):
    """
    Remove text inside parentheses () and brackets [] from the filename.
    """
    cleanup = re.sub(r"[\(\[].*?[\)\]]", "", filename_to_clean).split(" ")
    del cleanup[-2]
    print(f"Cleaned: '{filename_to_clean}' -> '{cleanup}'")
    cleanup.pop(-1)
    songEnd = cleanup.pop(-1)
    temp = " ".join(cleanup)
    return temp + " " + songEnd + ".mp3"

# Get the current directory
current_directory = os.getcwd()

# Loop through files in the current directory
for filename in os.listdir(current_directory):
    # Filter files: process only .mp3 files with () or [] in the name
    if filename.endswith(".mp3") and re.search(r"[\(\[]", filename):
        # Clean the filename
        cleaned_name = clean_filename(filename)
        if cleaned_name != filename:
            # Rename the file
            os.rename(filename, cleaned_name)
            print(f"Renamed: '{filename}' -> '{cleaned_name}'")

print("Filename cleanup complete!")
