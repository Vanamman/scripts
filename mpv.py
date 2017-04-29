#!/usr/bin/python3
#Ask user for link to a video, then streams that video in the best quality using the mpv video player

import subprocess

youtube = input("Please enter a video link: ")
quality = "--ytdl-format=bestvideo+bestaudio"

subprocess.call([r"/usr/bin/mpv", youtube, quality])
