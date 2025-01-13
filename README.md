# What is this?

These are two scripts that I made for myself to quickly download youtube videos as mp3s.
This script uses a yt-dlp.exe, instead of installing it. I don't like installing packages globally, because versions might get stuck. 

## Requirements
- Python 3.x
- yt-dlp executable (included in the same directory as the script)

## Installation
Clone this repository or download the script files.


``git clone https://github.com/your-username/your-repo-name.git``
Make sure the yt-dlp.exe is placed in the same directory as the script (or download it from the yt-dlp GitHub repository).


## Usage
Run the Script: Execute the youtube_dl.py script in your terminal:


``python youtube_dl.py``

After running the script, it will ask for a YouTube URL. Enter the URL of the video you want to download.Just copy paste it as you see the url.

Exit: To quit the script, enter q when prompted for a URL. It's not case sensitive.

When you exit it, you might see a random string of characters in a square bracket in a file name. Some songs also have other brackets included like with "(Original video)". I saw some compatibility issues in older MP3 players, so use cleanup.py to get rid of them.

``python cleanup.py``

## Future plans

It's probably really easy to structure this into one script, but at the time of writing, I have no real intention to do it. Maybe if it gives me that much friction while using it. 

### Acknowledgments
[Yt-dlp](https://github.com/yt-dlp/yt-dlp): It wouldn't be possible without the amazing people who work on this.