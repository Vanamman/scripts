#!/usr/bin/python3

#Small script that asks for twitch.tv channel name and quality, then proceeds to 
#run livestreamer with those variables in place 


import subprocess


print ("Channel name means only the name of the channel. twitch.tv/ is not needed")
print ("\n")


stream = input("Enter a twitch channel name: ")
quality = input('Enter a quality level (1080p60, 144p30, 240p30, 360p30, 480p30, 540p30, 720p30, 720p60, audio): ')

subprocess.call(["/usr/bin/livestreamer", 
	'twitch.tv/' + stream, quality])