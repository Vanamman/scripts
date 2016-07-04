import subprocess

youtube = input("Please enter a youtube link: ")
quality = "--ytdl-format=bestvideo+bestaudio"

subprocess.call([r"C:\Users\tott2\Documents\mpv\mpv.exe", youtube, quality])
