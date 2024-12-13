from moviepy.editor import AudioFileClip
import sys
import yt_dlp

# Function to download song from YouTube
def download_songs(*songs):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # Specify the download path and filename template
        'outtmpl': r'C:\Users\adhee\Documents\samples\youtube\%(title)s.%(ext)s',
    }

    for query in songs:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([f"ytsearch:{query}"])
            print(f"Downloaded and converted: {query}")
        except Exception as e:
            print(f"Failed to download {query}: {e}")


# Main entry point for command-line usage
if __name__ == "__main__":
    # Check if there are arguments passed
    if len(sys.argv) > 1:
        # Pass command-line arguments (excluding the script name) to the function
        download_songs(*sys.argv[1:])
    else:
        print("Please provide song titles to download.")

