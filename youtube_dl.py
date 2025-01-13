import subprocess
import os

# Get the path to yt-dlp executable in the same directory
yt_dlp_path = os.path.join(os.getcwd(), "yt-dlp.exe")

while True:
    # Prompt the user for a YouTube URL
    url = input("Enter the YouTube URL (or 'q' to quit): ")

    # Check if the user wants to quit
    if url.lower() == 'q':
        print("Exiting the script. Goodbye!")
        break

    # Define yt-dlp options for MP3 conversion
    OPTIONS = "--extract-audio --audio-format mp3"

    # Build the full command
    command = f'"{yt_dlp_path}" {OPTIONS} {url}'

    try:
        # Run the command
        subprocess.run(command, shell=True, check=True)
        print("MP3 download complete!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError:
        print("Error: Could not find 'yt-dlp.exe' in the current directory.")
        break
