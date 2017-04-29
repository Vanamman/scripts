#!/usr/bin/python3

#Download a video from many different websites. Not just YouTube.

import subprocess

youtube = input("Please enter a youtube link: ")
#quality = "--ytdl-format=bestvideo+bestaudio"

subprocess.call([r"/usr/bin/youtube-dl", youtube])